import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    # Sends a GET request to the homepage
    response = client.get('/')
    
    # Ensures that the request was successful (status 200)
    assert response.status_code == 200
    
    # Ensures that the word 'Todo' appears in the returned HTML
    assert b"Todo" in response.data