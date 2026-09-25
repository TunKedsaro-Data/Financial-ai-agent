FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install SQLite CLI
RUN apt-get update \
    && apt-get install -y --no-install-recommends sqlite3 tree\
    && rm -rf /var/lib/apt/lists/*

COPY backend/pyproject.toml ./pyproject.toml
COPY backend/src ./src
COPY backend/migrations ./migrations