#!/bin/bash

# Ottieni la cartella dove si trova lo script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Controlla se l'ambiente virtuale esiste
if [ ! -d "venv" ]; then
    echo "L'ambiente virtuale 'venv' non esiste. Lo creo ora..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installazione dipendenze..."
    pip install lancedb pandas sentence-transformers openai pypdf python-dotenv
else
    # Attiva l'ambiente virtuale
    source venv/bin/activate
fi

# Avvia il programma principale
python main.py
