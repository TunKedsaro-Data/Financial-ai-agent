# From python:3.12-slim-bookworm สร้าง Linux environment
FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
# WORKDIR /app = cd /app
WORKDIR /app
# apt install sqlite3 tree
# Install SQLite CLI
RUN apt-get update \
    && apt-get install -y --no-install-recommends sqlite3 tree \
    && rm -rf /var/lib/apt/lists/*
# Copy backend เอา source code เข้า Image
COPY backend/pyproject.toml ./pyproject.toml
COPY backend/src ./src
COPY backend/migrations ./migrations
# pip install . lib ต่างๆ
RUN pip install --no-cache-dir . \
    && useradd --create-home --uid 10001 appuser \
    && mkdir -p /data \
    && chown appuser:appuser /data

USER appuser

ENV DATABASE_PATH=/data/app.db \
    MIGRATIONS_PATH=/app/migrations

EXPOSE 8000

CMD ["uvicorn", "business_analyst.main:app", "--host", "0.0.0.0", "--port", "8000"]