import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_product_by_id():
    response = client.get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "price" in data

def test_get_product_not_found():
    response = client.get("/products/999999")
    assert response.status_code == 404

def test_create_product():
    new_product = {"name": "test_product", "price": 777}
    response = client.post("/products", json=new_product)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test_product"
    assert data["price"] == 777
    assert "id" in data