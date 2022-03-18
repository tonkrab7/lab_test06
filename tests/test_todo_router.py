from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app

client = TestClient(app)

def test_post_todo_insert(db):
    response = client.post(
        "/",
        json={
            "name": "string2",
            "description": "string",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "string2"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_post_todo_update(db):
    response = client.put(
        "/620b0f3e94c4ea6545622c80",
        json={
            "name": "update",
            "description": "string",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "update"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_post_todo_delete(db):
    response = client.delete(
        "/620b0f3e94c4ea6545622c80"
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

