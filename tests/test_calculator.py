from app.calculator import sum, resta, multiply
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sum()-> None:
    assert sum(2, 3) == 5

#introducir un fallo premeditado
def test_resta()-> None:
    assert resta(5, 3) == 2

def test_multiply()-> None:
    assert multiply(2, 3) == 6

def test_sum_endpoint() -> None:
    response = client.post("/sum", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == 5

def test_resta_endpoint() -> None:
    response = client.post("/resta", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == 2

def test_multiply_endpoint() -> None:
    response = client.post("/multiply", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == 6