def test_chat_app_entrypoint(client):
    response = client.get("/chat/")
    assert response.status_code == 200
