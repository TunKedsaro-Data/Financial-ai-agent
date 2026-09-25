from contextlib import asynccontextmanager
from fastapi import FastAPI
from business_analyst.core.config import Settings
from business_analyst.db.migrations import apply_migrations

# create FastAPI app with any input setting
def create_app(settings: Settings) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        apply_migrations(
            settings.database_path,
            settings.migrations_path,
        )
        yield

    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        lifespan=lifespan,
    )
    @app.get("/api/health")
    def health():
        return {
            "status": "ok",
            "service": settings.app_name,
            "version": settings.version,
        }
    return app


settings = Settings.from_env()
app = create_app(settings)