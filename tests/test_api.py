from fastapi.testclient import TestClient
import sys
from pathlib import Path

backend_path = Path(__file__).resolve().parents[1] / "backend"
sys.path.append(str(backend_path))

from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_generate():
    response = client.post("/generate", json={
        "resume_text": "Python FastAPI GitHub machine learning project",
        "target_role": "AI Intern"
    })
    assert response.status_code == 200
    assert "result" in response.json()
