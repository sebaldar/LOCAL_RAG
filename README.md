# LOCAL_RAG System - Indicizzazione e Chat con Documenti Personali

Un semplice sistema **Retrieval-Augmented Generation (RAG)** che permette di:

- Indicizzare documenti PDF, TXT e Markdown in un database vettoriale locale (LanceDB)
- Fare domande in linguaggio naturale sui contenuti indicizzati
- Ottenere risposte generate da **OpenAI GPT-4o-mini** con citazione delle fonti esatte (file, pagina approssimativa, riga)

Progettato per essere **leggero**, eseguibile anche su un Raspberry Pi 5 o su laptop con poca RAM.

## Caratteristiche principali

- Embedding con **all-MiniLM-L6-v2** (~80 MB di RAM)
- Database vettoriale locale con **LanceDB**
- Supporto per **PDF**, **.txt** e **.md**
- Splitting semplice del testo in blocchi di 5 righe
- Memoria contestuale di base (ultimi 3 scambi)
- Interfaccia menu testuale semplice
- Possibilità di resettare completamente il database

## Requisiti

- Python 3.9+
- Sistema operativo: Linux (testato su Raspberry Pi OS), Windows, macOS
- Connessione internet solo per le chiamate a OpenAI

### Librerie principali

```text
sentence-transformers
lancedb
pypdf
openai
python-dotenv
pandas

Installazione
    1. Clona il repository 
Bash
git clone https://github.com/sebaldar/LOCAL_RAG.git
cd RAG
    2. Crea un ambiente virtuale (consigliato) 
Bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
# oppure su Windows: venv\Scripts\activate
    3. Installa le dipendenze 
Bash
pip install -r requirements.txt
    4. Configura la chiave OpenAI 
Crea un file .env nella root del progetto:
env
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Puoi ottenere la chiave da: https://platform.openai.com/api-keys
Utilizzo
Avvia il programma principale:
Bash
python main.py
Menu disponibile
text
MATHEMATIC - RAG SYSTEM   
==============================
1.  INDICIZZA DOCUMENTI (Aggiorna DB)
2.  AVVIA CHAT (OpenAI)
3.  RESET DATABASE (Cancella tutto)
4. ❌ ESCI
==============================
    1. Indicizza documenti
        ◦ Metti i tuoi file PDF, TXT o MD nella cartella ./documenti 
        ◦ Scegli opzione 1 → crea/aggiorna il database vettoriale in ./my_knowledge_base 
    2. Avvia chat
        ◦ Scegli opzione 2 
        ◦ Scrivi le tue domande 
        ◦ Digita esci, quit o exit per terminare 
    3. Reset database
        ◦ Cancella completamente la knowledge base (utile per ripartire da zero) 
Struttura del progetto
text
RAG/
├── main.py               # Menu principale e launcher
├── indicizza.py          # Script di indicizzazione documenti → LanceDB
├── chat_rag.py           # Interfaccia chat RAG con OpenAI
├── requirements.txt      # Dipendenze Python
├── .gitignore
├── .env.example          # (opzionale) esempio per la chiave API
├── documenti/            # ← Qui metti i tuoi PDF, txt, md
└── my_knowledge_base/    # Database vettoriale LanceDB (creato automaticamente)
Note importanti
    • Il modello di embedding (all-MiniLM-L6-v2) è molto leggero e funziona bene anche su Raspberry Pi. 
    • La ricerca è basata su similarità vettoriale (cosine similarity implicita in LanceDB). 
    • Il sistema non fa chunking avanzato (es. con overlap o per frasi). Per documenti molto complessi potresti voler migliorare lo splitting. 
    • Attualmente la paginazione PDF è approssimativa (basata sul numero di blocchi). 
    • Non caricare documenti sensibili su repository pubblici. 
Miglioramenti futuri possibili
    • Chunking più intelligente (con LangChain o LlamaIndex) 
    • Supporto per immagini / OCR nei PDF 
    • Scelta del modello embedding più potente 
    • Interfaccia web con Streamlit o Gradio 
    • Gestione multi-tabella / multi-documento 
    • Ricerca ibrida (keyword + vettoriale) 
Licenza
MIT License (oppure scegli la licenza che preferisci)

Realizzato su Raspberry Pi 5 Autore: Sergio Baldaro (sebaldar)

