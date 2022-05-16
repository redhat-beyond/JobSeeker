from job_board.models.job_type import JobType
from job_board.models.location import Location
from job_board.models.preference import Preference
import pytest


@pytest.fixture
def create_data_models_instances():
    job_type = JobType.objects.create(text='Chef')
    location = Location.objects.create(name='city', latitude=29.559191910075217, longitude=34.95283437084102)
    pref = Preference.objects.create(
        job_type=JobType.objects.first(),
        location=Location.objects.first(),
        years_of_experience=Preference.yearsOfExperience.YEARS5ANDABOVE,
        work_schedule=Preference.workSchedule.FULLTIME)

    return [job_type, location, pref]


@pytest.mark.usefixtures("create_data_models_instances")
@pytest.mark.django_db
class TestJobBoardModels:

    def test_data_creation(self, create_data_models_instances):
        job_type = create_data_models_instances[0]
        location = create_data_models_instances[1]
        preference = create_data_models_instances[2]

        assert JobType.objects.filter(text=job_type).exists()

        assert Location.objects.filter(
            name=location.name,
            latitude=location.latitude,
            longitude=location.longitude).exists()

        assert Preference.objects.filter(
            job_type=preference.job_type,
            location=preference.location,
            years_of_experience=preference.years_of_experience,
            work_schedule=preference.work_schedule).exists()

    def test_data_deletion(self, create_data_models_instances):
        job_type = JobType.objects.filter(text=create_data_models_instances[0].text).first()
        location = Location.objects.filter(
            name=create_data_models_instances[1].name,
            latitude=create_data_models_instances[1].latitude,
            longitude=create_data_models_instances[1].longitude).first()
        preference = Preference.objects.filter(id=create_data_models_instances[2].id).first()

        job_type.delete()
        assert job_type not in JobType.objects.all()

        location.delete()
        assert location not in Location.objects.all()

        preference.delete()
        assert preference not in Preference.objects.all()
