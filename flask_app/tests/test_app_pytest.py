
'''
calling test 
set PYTHONPATH=D:\working\tryouts\flask_app
pytest -vs

'''


import pytest
import json
from app import app

# --------- Option 1 -----------------------------------------
def test_print_example():
    print("🚀 This is a print statement inside a test!")
    assert 1 == 1

class TestSample:
    def setup_method(self):
        print("\nSetting up before a test method")

    def teardown_method(self):
        print("\nTearing down after a test method")

    def test_addition(self):
        result = 2 + 3
        assert result == 5

    def test_subtraction(self):
        result = 5 - 2
        assert result == 3

# ------------------------------------------------------------


# --------- Option 2 -----------------------------------------

@pytest.fixture
def client():
    """Set up a test client for the app with setup and teardown logic."""
    print("\nSetting up the test client")
    with app.test_client() as client:
        yield client  # This is where the testing happens
    print("Tearing down the test client")


def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    #assert response.json == {"message": "Hello, Flask!"}
    assert response.text == "Flask is working"

def test_post(client):
    """Test the home route."""
    print('===================test_post')
    data={"first_name": "Anu", "last_name": "Mohan"} 
    response = client.post('/profile/add', json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Missing required fields in validator"}


def _sample_asserts(client):  
    response = client.get('/')

    assert response.status_code == 200
    assert response.text == "Flask is working"
    assert response.json == {"message": "This is the About page"}

    





# 🚀 What are Fixtures in Pytest?
# - They return some data or object that your test can use.
@pytest.fixture
def numbers():
    return (10, 20)

def test_addition(numbers):
    x, y = numbers
    assert x + y == 30


