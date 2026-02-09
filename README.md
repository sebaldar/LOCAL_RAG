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

📋 Menu disponibile
RAG SYSTEM
==============================
1.  INDICIZZA DOCUMENTI (Aggiorna DB)
2.  AVVIA CHAT (OpenAI)
3.  RESET DATABASE (Cancella tutto)
4.  ❌ ESCI
==============================

1️⃣ Indicizza documenti

Inserisci i file PDF / TXT / MD nella cartella ./documenti

Seleziona l’opzione 1

Il database vettoriale viene creato/aggiornato in ./my_knowledge_base

2️⃣ Avvia chat

Seleziona l’opzione 2

Scrivi le tue domande in linguaggio naturale

Digita esci, quit o exit per terminare

3️⃣ Reset database

Cancella completamente la knowledge base

Utile per ripartire da zero o cambiare documenti

📁 Struttura del progetto
RAG/
├── main.py               # Menu principale e launcher
├── indicizza.py          # Indicizzazione documenti → LanceDB
├── chat_rag.py           # Chat RAG con OpenAI
├── requirements.txt      # Dipendenze Python
├── .gitignore
├── .env.example          # Esempio file ambiente
├── documenti/            # ← Inserire qui PDF / TXT / MD
└── my_knowledge_base/    # Database vettoriale LanceDB

⚠️ Note importanti

Il modello all-MiniLM-L6-v2 è molto leggero e adatto a Raspberry Pi

La ricerca usa similarità vettoriale (cosine similarity in LanceDB)

Il sistema non utilizza chunking avanzato (no overlap, no frasi)

La paginazione PDF è approssimativa (basata sul numero di chunk)

Non caricare documenti sensibili su repository pubblici

🔮 Miglioramenti futuri possibili

Chunking più intelligente (LangChain / LlamaIndex)

OCR e supporto immagini nei PDF

Modelli di embedding più potenti

Interfaccia web (Streamlit / Gradio)

Supporto multi-database / multi-documento

Ricerca ibrida (keyword + vettoriale)

📜 Licenza

MIT License

👤 Autore

Sergio Baldaro
GitHub: https://github.com/sebaldar

Realizzato e testato su Raspberry Pi 5 🥧
