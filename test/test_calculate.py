from fastapi.testclient import TestClient
from starlette import status
from app.main import app

client = TestClient(app)

def test_add():
    response = client.post('/add/?a=5&b=2')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'result': 7}