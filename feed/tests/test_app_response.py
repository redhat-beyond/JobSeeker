import pytest
from django.db.models.query import QuerySet


FEED_URL = '/'


@pytest.mark.django_db
def test_feed_page_entrypoint(client):
    response = client.get(FEED_URL)
    assert response.status_code == 200


@pytest.mark.django_db
def test_feed_context(client):
    response = client.get(FEED_URL)
    context = response.context
    assert isinstance(context['posts'], QuerySet)
    assert context['posts'].count() > 0
    assert context['title'] == 'Feed'
