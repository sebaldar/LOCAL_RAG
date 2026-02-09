import os
import lancedb
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# 1. Configurazione
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
MODEL_OPENAI = "gpt-4o-mini"
PATH_DB = "./my_knowledge_base"
NOME_TABELLA = "knowledge_dettagliata"

if not api_key:
    print("ERRORE: Chiave OPENAI_API_KEY non trovata.")
    exit()

# 2. Inizializzazione Modelli (Leggeri per la RAM)
client = OpenAI(api_key=api_key)
# Questo modello occupa solo ~80MB di RAM
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Connessione al Database
db = lancedb.connect(PATH_DB)
try:
    table = db.open_table(NOME_TABELLA)
    print(f"Database pronto. Usando {MODEL_OPENAI} via API.")
except:
    print("Tabella non trovata. Esegui prima lo script di indicizzazione!")
    exit()

chat_history = []

# --- LOGICA DI SUPPORTO ---

def cerca_contesto(query, top_n=3):
    """Cerca i frammenti più rilevanti in locale."""
    query_vec = embed_model.encode(query).tolist()
    # Esegue la ricerca vettoriale su LanceDB
    result = table.search(query_vec).limit(top_n).to_pandas()
    
    context_text = ""
    for _, row in result.iterrows():
        # Gestione flessibile dei metadati
        meta = f"[FILE: {row['source']}"
        if 'pagina' in row: meta += f", PAG: {row['pagina']}"
        if 'riga' in row: meta += f", RIGA: {row['riga']}"
        meta += "]"
        context_text += f"\n{meta}\n{row['text']}\n"
    return context_text

# --- CICLO DI CHAT ---

while True:
    domanda = input("\nDomanda (o 'esci'): ")
    if domanda.lower() in ['esci', 'quit', 'exit']: break

    # 1. Recupero contesto locale (VPS/PC)
    contesto = cerca_contesto(domanda)

    # 2. Gestione Memoria (ultimi 3 scambi per dare continuità)
    memoria_scambi = ""
    for scambio in chat_history[-3:]:
        memoria_scambi += f"User: {scambio['q']}\nAI: {scambio['a']}\n"

    # 3. Costruzione Prompt per OpenAI
    prompt_finale = f"""Sei un assistente esperto. Rispondi alla DOMANDA dell'utente usando il CONTESTO fornito e tenendo conto della CRONOLOGIA.
Cita sempre la fonte esatta (File, Pagina, Riga) se presente nel contesto.

CRONOLOGIA:
{memoria_scambi}

CONTESTO RECUPERATO:
{contesto}

DOMANDA:
{domanda}"""

    # 4. Chiamata a OpenAI
    try:
        response = client.chat.completions.create(
            model=MODEL_OPENAI,
            messages=[
                {"role": "system", "content": "Rispondi in modo conciso e cita le fonti."},
                {"role": "user", "content": prompt_finale}
            ],
            temperature=0.2 # Bassa temperatura = risposte più precise e meno creative
        )
        risposta_ai = response.choices[0].message.content
        
        print("\n--- RISPOSTA AI ---")
        print(risposta_ai)

        # Aggiorna la storia locale
        chat_history.append({"q": domanda, "a": risposta_ai})

    except Exception as e:
        print(f"Errore durante la chiamata OpenAI: {e}")
