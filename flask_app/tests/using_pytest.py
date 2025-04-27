import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data


def test_print_example():
    print("🚀 This is a print statement inside a test!")
    assert 1 == 1



# pytest -v
# pytest tests/test_app.py
# pytest -v --log-cli-level=INFO

#pytest -s tests/pytest_app.py