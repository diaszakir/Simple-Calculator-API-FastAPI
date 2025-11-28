from fastapi.testclient import TestClient
from starlette import status
from app.main import app
import pytest

client = TestClient(app)

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 7),
    (-2, -4, -6),
    (10, -3, 7)
])

def test_add(a, b, expected):
    response = client.post(f'/add/?a={a}&b={b}')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'result': expected}

def test_add_not_number():
    response = client.post('/add/?a=t&b=c')
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

@pytest.mark.parametrize('a, b, expected', [
    (3, 2, 1),
    (-1, -5, 4),
    (3, -7, 10)
])

def test_sub(a, b, expected):
    response = client.post(f'/sub/?a={a}&b={b}')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'result': expected}

def test_sub_not_number():
    response = client.post('/sub/?a=t&b=c')
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 2),
    (2, 3, 6),
    (-4, 2, -8),
    (-6, -2, 12),
    (6, -2, -12)
])

def test_multiply(a, b, expected):
    response = client.post(f'/multiply/?a={a}&b={b}')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'result': expected}

def test_multiply_not_number():
    response = client.post('/multiply/?a=b&b=c')
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT