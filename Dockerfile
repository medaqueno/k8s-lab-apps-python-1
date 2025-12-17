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

COPY src/ ./src/

# 2. Aseguramos que el PYTHONPATH incluya la carpeta src
ENV PYTHONPATH=/app/src

# 3. Ejecutamos desde la carpeta src
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]