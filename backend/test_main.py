import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/token", data={"username": "usuario", "password": "senha123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_failure():
    response = client.post("/token", data={"username": "usuario", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Credenciais inválidas"

def test_read_users_me():
    login_response = client.post("/token", data={"username": "usuario", "password": "senha123"})
    access_token = login_response.json()["access_token"]
    
    response = client.get("/users/me", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "usuario"
    assert response.json()["full_name"] == "Usuário Teste"
    assert response.json()["email"] == "usuario@email.com"

def test_read_users_me_unauthorized():
    response = client.get("/users/me")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"
