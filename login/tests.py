def test_login_app_entrypoint(client):
    response = client.get("/login/")
    assert response.status_code == 200
