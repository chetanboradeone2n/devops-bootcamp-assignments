from app import app

# Create a test client
client = app.test_client()

def test_healthcheck():
    response = client.get("/api/v1/healthcheck")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
