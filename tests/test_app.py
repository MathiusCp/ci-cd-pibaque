import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

def test_home():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert "Aplicación Flask funcionando correctamente" in response.get_data(as_text=True)

def test_ia():
    tester = app.test_client()
    response = tester.post("/ia", json={"prompt": "hola"})
    assert response.status_code == 200
    assert "IA Response to: hola" in response.get_data(as_text=True)
