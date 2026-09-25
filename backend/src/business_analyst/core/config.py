import os
from dataclasses import dataclass
from pathlib import Path

def _default_migrations_path() -> Path:
    return Path(__file__).resolve().parents[3]/"migrations"

@dataclass(frozen=True)
class Settings:
    app_name: str = "Financial AI Agent"
    version: str = "0.1.0"
    database_path: Path = Path(".local/app.db")
    migrations_path: Path = _default_migrations_path()

    @classmethod
    def from_env(cls):
        return cls(
            app_name=os.getenv("APP_NAME","Financial AI Agent",),
            version=os.getenv("APP_VERSION","0.1.0"),
            database_path=Path(os.getenv("DATABASE_PATH",".local/app.db")),
            migrations_path=Path(os.getenv("MIGRATIONS_PATH",str(_default_migrations_path()),)),
            )