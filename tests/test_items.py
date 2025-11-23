from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list_items():
    # Add item
    response = client.post("/items", json={"id": 1, "name": "apple", "price": 2.50})
    assert response.status_code == 200
    assert response.json()["item"]["name"] == "apple"

    # Retrieve items
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_item():
    response = client.post("/items", json={"id": 1, "name": "apple", "price": 2.50})
    assert response.status_code == 200
    assert response.json()["item"]["name"] == "apple"
    
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "apple"

def test_get_missing_item():
    response = client.get("/items/2")
    assert response.status_code == 404