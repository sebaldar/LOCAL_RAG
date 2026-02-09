#!/bin/bash

# Ottieni la cartella dove si trova lo script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Crea la cartella documenti se non esiste
mkdir -p documenti

# Controlla se l'ambiente virtuale esiste
if [ ! -d "venv" ]; then
    echo "--- Creazione ambiente virtuale 'venv' ---"
    python3 -m venv venv
    source venv/bin/activate
    echo "--- Aggiornamento pip ---"
    pip install --upgrade pip
    echo "--- Installazione dipendenze ---"
    # Uso il file requirements.txt se esiste, altrimenti i nomi delle librerie
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    else
        pip install lancedb pandas sentence-transformers openai pypdf python-dotenv
    fi
else
    echo "--- Attivazione ambiente virtuale ---"
    source venv/bin/activate
fi

# Avvia il programma principale
echo "--- Avvio in corso... ---"
python3 main.py
