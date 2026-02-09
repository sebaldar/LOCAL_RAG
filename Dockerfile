# Usa un'immagine Python leggera per architettura ARM
FROM python:3.11-slim

# Installa le dipendenze di sistema necessarie per compilare alcune librerie AI
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crea la cartella di lavoro nel container
WORKDIR /app

# Copia i requisiti e installali
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del codice
COPY . .

# Comando predefinito (permette di interagire con il menu)
CMD ["python", "main.py"]
