import pytest
from pytest_django.asserts import assertTemplateUsed, assertTemplateNotUsed

JOB_BOARD_URL = '/job_board/'
POST_TEMPLATE = 'job_board/post.html'


@pytest.fixture
def create_valid_form_data():
    form1 = {
        'job_type': '1',
        'location': '3',
        'years_of_experience': 'no experience',
        'work_schedule': 'Flexible'
    }

    return [form1]


@pytest.fixture
def create_invalid_form_data():
    form1 = {
        'job_type': '-3',
        'location': '2',
        'years_of_experience': '5+ years',
        'work_schedule': 'Not specified'
    }

    return [form1]


@pytest.mark.django_db
class TestSearchView():

    def test_get_request(self, client):
        response = client.get(JOB_BOARD_URL)
        assert response.status_code == 200
        assertTemplateNotUsed(response, POST_TEMPLATE)

    def test_search_using_valid_form(self, client, create_valid_form_data):
        form1_data = create_valid_form_data[0]
        response = client.post(JOB_BOARD_URL, form1_data)
        assert response.status_code == 200
        assertTemplateUsed(response, POST_TEMPLATE)

    def test_search_using_invalid_form(self, client, create_invalid_form_data):
        form1_data = create_invalid_form_data[0]
        response = client.post(JOB_BOARD_URL, form1_data)
        assert response.status_code == 200
        assertTemplateNotUsed(response, POST_TEMPLATE)
