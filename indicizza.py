import lancedb
import os
import pandas as pd
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

# --- CONFIGURAZIONE ---
NOME_TABELLA = "knowledge_dettagliata"
CARTELLA_DOCS = "./documenti"
PATH_DB = "./my_knowledge_base"

print("Inizializzazione modello di embedding (all-MiniLM-L6-v2)...")
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def indicizza_documenti():
    if not os.path.exists(CARTELLA_DOCS):
        os.makedirs(CARTELLA_DOCS)
        print(f"Cartella '{CARTELLA_DOCS}' creata. Inserisci i file.")
        return None

    db = lancedb.connect(PATH_DB)
    documenti_per_db = []
    
    file_presenti = [f for f in os.listdir(CARTELLA_DOCS) if f.endswith(('.pdf', '.txt', '.md'))]
    
    if not file_presenti:
        print("Nessun file compatibile trovato in 'documenti'.")
        return None

    for filename in file_presenti:
        percorso = os.path.join(CARTELLA_DOCS, filename)
        print(f" Elaborazione: {filename}...")
        
        testo_estratto = ""
        if filename.endswith(".pdf"):
            reader = PdfReader(percorso)
            for pagina in reader.pages:
                testo_estratto += pagina.extract_text() + "\n"
        else: # txt o md
            with open(percorso, "r", encoding="utf-8") as f:
                testo_estratto = f.read()

        # Splitting semplice e creazione vettori
        righe = [r for r in testo_estratto.split('\n') if len(r.strip()) > 20]
        passo = 5
        for i in range(0, len(righe), passo):
            blocco = " ".join(righe[i:i+passo])
            vector = embed_model.encode(blocco).tolist()
            documenti_per_db.append({
                "vector": vector,
                "text": blocco,
                "source": filename,
                "pagina": (i // 10) + 1, # Approssimativo per PDF
                "riga": i + 1
            })

    if documenti_per_db:
        print(f"Salvataggio di {len(documenti_per_db)} blocchi in LanceDB...")
        # Crea la tabella (sovrascrive se esiste)
        return db.create_table(NOME_TABELLA, documenti_per_db, mode="overwrite")
    return None

if __name__ == "__main__":
    table = indicizza_documenti()
    if table:
        print("✅ INDICIZZAZIONE COMPLETATA!")
    else:
        print("❌ Operazione fallita.")
