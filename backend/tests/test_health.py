from pathlib import Path
from fastapi.testclient import TestClient
from business_analyst.core.config import Settings
from business_analyst.main import create_app

def test_health_endpoint(tmp_path: Path):
    """Test the health endpoint with a temporary database."""
    migrations_path = (Path(__file__).resolve().parents[1]/ "migrations")
    settings = Settings(
        app_name="Financial AI Agent",
        version="0.1.0",
        database_path=tmp_path / "app.db",
        migrations_path=migrations_path,
    )
    app = create_app(settings)
    with TestClient(app) as client:
        response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "Financial AI Agent",
        "version": "0.1.0",
    }



# from fastapi.testclient import TestClient
# from business_analyst.main import app

# def test_health_endpoint():
#     with TestClient(app) as client:
#         response = client.get("/api/health")
#     assert response.status_code == 200
#     assert response.json() == {
#         "status": "ok",
#         "service": "Financial AI Agent",
#         "version": "0.1.0",
#     }