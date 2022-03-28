import pytest
import django.contrib.auth

def test_profile_app_entrypoint(client):
    response = client.get("/profile/")
    assert response.status_code == 200