from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_leer_raiz():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "¡Hola desde FastAPI!"}
