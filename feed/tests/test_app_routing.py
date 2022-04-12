import pytest


@pytest.mark.django_db
def test_feed_app_entrypoint(client):
    response = client.get("")
    assert response.status_code == 200
