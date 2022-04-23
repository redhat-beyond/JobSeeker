from job_board.search_form import SearchForm
from django.test import RequestFactory
import pytest

valid_form_datas = [
    {
        'job_type': '1',
        'location': '1',
        'years_of_experience': '0-2 years',
        'work_schedule': 'Flexible'
    },
    {
        'job_type': '3',
        'location': '2',
        'years_of_experience': '5+ years',
        'work_schedule': 'Not specified'
    }
]

invalid_form_datas = [
    {
        'job_type': '100'
    },
    {
        'job_type': '-3',
        'location': '2',
        'years_of_experience': '5+ years',
        'work_schedule': 'Not specified'
    }
]
job_board_url = '/job_board/'


@pytest.fixture
def create_valid_form_instances():
    request1 = RequestFactory().post(job_board_url, valid_form_datas[0])
    form1 = SearchForm(request1.POST)
    request2 = RequestFactory().post(job_board_url, valid_form_datas[1])
    form2 = SearchForm(request2.POST)

    return [form1, form2]


@pytest.fixture
def create_invalid_form_instances():
    request1 = RequestFactory().post(job_board_url, invalid_form_datas[0])
    form1 = SearchForm(request1.POST)
    request2 = RequestFactory().post(job_board_url, invalid_form_datas[1])
    form2 = SearchForm(request2.POST)

    return [form1, form2]


@pytest.mark.django_db
class TestSearchForm():

    def test_search_valid_form(self, create_valid_form_instances):
        form1 = create_valid_form_instances[0]
        form2 = create_valid_form_instances[1]

        assert form1.is_valid()
        assert form2.is_valid()

    def test_search_invalid_form(self, create_invalid_form_instances):
        form1 = create_invalid_form_instances[0]
        form2 = create_invalid_form_instances[1]

        assert not form1.is_valid()
        assert not form2.is_valid()
