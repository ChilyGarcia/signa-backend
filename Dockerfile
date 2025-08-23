FROM python:3.12-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_MODULE=app.main:app \
    WORKERS=2 \
    PORT=8000

# Dependencias del sistema (para uvicorn[standard], psycopg2, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates \
    libpq-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Crear usuario no-root
RUN useradd -m appuser
WORKDIR /app

# Copiar archivo de configuración alembic.ini
COPY alembic.ini /app/alembic.ini

# Instalar dependencias
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la estructura de la aplicación
COPY app /app/app
RUN chown -R appuser:appuser /app
USER appuser

# Comando: Gunicorn + UvicornWorker
CMD exec gunicorn "$APP_MODULE" \
    --workers "$WORKERS" \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:"$PORT" \
    --timeout 60 \
    --graceful-timeout 30 \
    --keep-alive 5 \
    --access-logfile - \
    --error-logfile -
