from job_board.views import AddSearchView
from django.test import RequestFactory
import pytest


@pytest.mark.django_db
class TestJobBoardURLs:
    def test_job_board_app_entrypoint(self, client):
        request = RequestFactory().get('/job_board/')
        response = AddSearchView.as_view()(request)
        assert response.status_code == 200
