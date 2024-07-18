from fastapi.testclient import TestClient
from main import app


# add basic test to test pytest
def test_read_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "app_name-service-ms v1"
