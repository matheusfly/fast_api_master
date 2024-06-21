from fastapi.testclient import TestClient
from api_master import app
from http import HTTPStatus



async def test_read_root_return_ok_hello():
    client = TestClient(app)
    
    response = client.get('/') 

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}