import pytest

from src import create_app


@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Welcome to memchess!'
