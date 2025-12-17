# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código (asumiendo que main.py está en la raíz o ajusta según tu estructura)
COPY . .

# NO copiamos .env explícitamente (se ignora vía .dockerignore o no debería existir en build)

ENV PYTHONPATH=/app
EXPOSE 8000

# Ajuste del comando: si main.py está en la raíz, es "main:app", si está en src, es "src.main:app"
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]