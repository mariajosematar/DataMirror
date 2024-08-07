from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_connect_user():
    response = client.post("/connect", json={
        "user_id": "123",
        "name": "John Doe",
        "email": "john@example.com",
        "connected_services": ["github"]
    })
    assert response.status_code == 200
    assert response.json() == {"message": "User John Doe connected successfully"}
