import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    # שולח בקשת GET לעמוד הבית
    response = client.get('/')
    
    # מוודא שהבקשה הצליחה (סטטוס 200)
    assert response.status_code == 200
    
    # מוודא שהמילה 'Todo' מופיעה ב-HTML שחוזר
    assert b"Todo" in response.data