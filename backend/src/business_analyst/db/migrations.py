import sqlite3
from pathlib import Path

def connect(database_path:Path) -> sqlite3.Connection:
    ''' เปิด Database '''
    database_path.parent.mkdir(parents=True,exist_ok=True,)
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def apply_migrations(database_path: Path,migrations_path: Path)->None:
    ''' ทำให้ Database schema เป็น version ล่าสุด '''
    with connect(database_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version TEXT PRIMARY KEY
            )
            """
        )
        applied_versions = {
            row["version"]
            for row in connection.execute(
                "SELECT version FROM schema_migrations"
            )
        }
        migration_files = sorted(migrations_path.glob("*.sql"))
        for migration_file in migration_files:
            version = migration_file.name
            if version in applied_versions:
                continue
            sql = migration_file.read_text(encoding="utf-8")
            connection.executescript(sql)
            connection.execute(
                """
                INSERT INTO schema_migrations (version)
                VALUES (?)
                """,
                (version,),
            )
        connection.commit()

def migration_count(database_path:Path) -> int:
    ''' ถามว่า Database นี้ apply migration ไปกี่ตัวแล้ว '''
    with connect(database_path) as connection:
        return connection.execute(
            "SELECT COUNT(*) FROM schema_migrations"
        ).fetchone()[0]