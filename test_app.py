from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, DevOps World! v1' in response.data