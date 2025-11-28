from fastapi.testclient import TestClient
from app.main import app
from starlette import status

client = TestClient(app)

def test_api():
    response = client.get("/test")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "OK"}