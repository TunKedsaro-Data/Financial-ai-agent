from fastapi import FastAPI

from contextlib import asynccontextmanager

from business_analyst.core.config import Settings
from business_analyst.db.migrations import apply_migrations

settings = Settings.from_env()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # apply migration
    apply_migrations(
        settings.database_path,
        settings.migrations_path
    )
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    lifespan=lifespan
)

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.version
    }