def test_login_app_entrypoint(client):
    response = client.get("/login/")
    assert response.status_code == 200

def test_logout_link(self, client, user):
        client.force_login(user)
        response = client.get('/logout/')
        response = client.get(response.url)
        assert response.context['user'].is_anonymous
        