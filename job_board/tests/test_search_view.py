import pytest


valid_form_data = [
    {
        'job_type': '1',
        'location': '3',
        'years_of_experience': 'no experience',
        'work_schedule': 'Flexible'
    },
]

invalid_form_data = [
    {
        'job_type': '-3',
        'location': '2',
        'years_of_experience': '5+ years',
        'work_schedule': 'Not specified'
    }
]

JOB_BOARD_URL = '/job_board/'


@pytest.mark.django_db
class TestSearchView():

    def test_get_request(self, client):
        response = client.get(JOB_BOARD_URL)
        assert response.status_code == 200

    def test_search_using_valid_form(self, client):
        response = client.post(JOB_BOARD_URL, valid_form_data[0])
        assert response.status_code == 200

    def test_search_using_invalid_form(self, client):
        response = client.post(JOB_BOARD_URL, invalid_form_data[0])
        assert response.status_code == 200
