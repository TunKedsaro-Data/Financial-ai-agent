import sqlite3
from pathlib import Path

from business_analyst.db.migrations import apply_migrations


def test_apply_migrations_is_idempotent(tmp_path: Path):
    database_path = tmp_path / "app.db"
    migrations_path = (Path(__file__).resolve().parents[1] / "migrations")

    # Idempotency test: running the migration twice should produce the same final state.    apply_migrations(database_path,migrations_path,)
    apply_migrations(database_path,migrations_path,)
    apply_migrations(database_path,migrations_path,)

    with sqlite3.connect(database_path) as connection:
        migration_count = connection.execute(
            """
            SELECT COUNT(*)
            FROM schema_migrations
            """
        ).fetchone()[0]
        schema_generation = connection.execute(
            """
            SELECT value
            FROM app_metadata
            WHERE key = 'schema_generation'
            """
        ).fetchone()[0]
    assert migration_count == 1
    assert schema_generation == "walking-skeleton"