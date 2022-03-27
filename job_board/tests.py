from job_board.models.job_type import JobType
from job_board.models.location import Location
from job_board.models.years_of_experience import YearsOfExperience
from job_board.models.preference import Preference
import pytest


@pytest.fixture
def create_data_models_instances():
    JobType.objects.create(text='Chef')
    Location.objects.create(name='Eilat', latitude=29.559191910075217, longitude=34.95283437084102)
    YearsOfExperience.objects.create(text='5-10 years')
    Preference.objects.create(
        job_type=JobType.objects.first(),
        location=Location.objects.first(),
        years_of_experience=YearsOfExperience.objects.first())


@pytest.mark.usefixtures("create_data_models_instances")
@pytest.mark.django_db
class TestJobBoardModels:

    def test_data_creation(self):
        assert JobType.objects.filter(text='Chef').exists()

        assert Location.objects.filter(name='Eilat', latitude=29.559191910075217, longitude=34.95283437084102).exists()

        assert YearsOfExperience.objects.filter(text='5-10 years').exists()

        assert Preference.objects.filter(
            job_type=JobType.objects.first(),
            location=Location.objects.first(),
            years_of_experience=YearsOfExperience.objects.first()).exists()

    def test_data_deletion(self):
        JobType.objects.filter(text='Web developer').delete()
        assert not JobType.objects.filter(text='Web developer').exists()

        Location.objects.filter(name='Haifa', latitude=32.804135934085565, longitude=34.98975968417104).delete()
        assert not Location.objects.filter(
            name='Haifa',
            latitude=32.804135934085565,
            longitude=34.98975968417104).exists()

        YearsOfExperience.objects.filter(text='0-2 years').delete()
        assert not YearsOfExperience.objects.filter(text='0-2 years').exists()

        Preference.objects.filter(
            job_type=JobType.objects.first(),
            location=Location.objects.first(),
            years_of_experience=YearsOfExperience.objects.first()).delete()
        assert not Preference.objects.filter(
            job_type=JobType.objects.first(),
            location=Location.objects.first(),
            years_of_experience=YearsOfExperience.objects.first()).exists()
