import pytest
import django.contrib.auth
import datetime
from .models import PersonalProfile
from django.core.files.uploadedfile import SimpleUploadedFile


IMAGE_PATH = 'personal_profile/static/personal_profile/images/test_image.jpg'
User = django.contrib.auth.get_user_model()


def test_profile_app_entrypoint(client):
    response = client.get("/profile/")
    assert response.status_code == 200


@pytest.fixture()
def user_1(db):
    return User.objects.create_user('user_1', password='userpassword')


@pytest.fixture()
def profile_1(db, user_1):
    profile_1 = PersonalProfile(company='Test Company', user=user_1, about='Test About',
                                birth_date=datetime.date(1995, 12, 10),
                                profile_pic=SimpleUploadedFile(name='test_image.jpg',
                                                               content=open(IMAGE_PATH, 'rb').read(),
                                                               content_type='image/jpeg'),
                                resume=SimpleUploadedFile('test_resume.txt',
                                                          b'these are the contents of the txt file'))
    return profile_1


class TestProfileModel:
    # Testing different Personal Profile attributes

    def test_newprofile(self, profile_1, user_1):
        assert profile_1.company == 'Test Company'
        assert profile_1.user == user_1
        assert profile_1.about == 'Test About'
        assert profile_1.birth_date == datetime.date(1995, 12, 10)
        assert profile_1.profile_pic is not None
        assert profile_1.resume is not None
