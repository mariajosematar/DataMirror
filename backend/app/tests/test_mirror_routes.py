from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_mirror_interface():
    response = client.get("/mirror_interface")
    assert response.status_code == 200
    assert response.json() == {
        "gesture_controls": ["swipe", "tap", "wave"],
        "holographic_assistant": "active"
    }

def test_create_digital_twin():
    response = client.post("/create_digital_twin", json={"user_id": "123"})
    assert response.status_code == 200
    assert response.json() == {
        "instagram_data": {"followers": 500, "posts": 100},
        "facebook_data": {"friends": 300, "likes": 1000},
        "gmail_data": {"emails_per_day": 50, "contacts": 200}
    }
