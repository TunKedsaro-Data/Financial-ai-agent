from fastapi import FastAPI
from business_analyst.core.config import Settings

settings = Settings.from_env()

app = FastAPI(
    title=settings.app_name,
    version=settings.version
)

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.version
    }