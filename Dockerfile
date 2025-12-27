# Image Python officielle légère
FROM python:3.12-slim

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean

# Copier les dépendances Python
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port FastAPI
EXPOSE 8000

# Lancer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]
