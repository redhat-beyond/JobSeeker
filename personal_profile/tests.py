import pytest
import django.contrib.auth
import datetime
from django.contrib.auth.models import User
from .models import PersonalProfile
from django.core.files.uploadedfile import SimpleUploadedFile


IMAGE_PATH = 'personal_profile/static/personal_profile/images/profile_pics/test_image.jpg'
User = django.contrib.auth.get_user_model()


def test_profile_app_entrypoint(client):
    response = client.get("/profile/")
    assert response.status_code == 200


@pytest.fixture()
def user_1(db):
    user_1 = User.objects.create_user('user_1', password='userpassword')
    user_1.save()
    return user_1


@pytest.fixture()
def profile_1(db, user_1):
    profile_1 = PersonalProfile(company='Test Company', user=user_1, about='Test About',
                                birth_date=datetime.date(1995, 12, 10),
                                profile_pic=SimpleUploadedFile(name='test_image.jpg',
                                                               content=open(IMAGE_PATH, 'rb').read(),
                                                               content_type='image/jpeg'),
                                resume=SimpleUploadedFile('test_resume.txt',
                                                          b'these are the contents of the txt file'))
    profile_1.save()
    return profile_1


@pytest.mark.django_db
class TestProfileModel:
    # Testing different Personal Profile saving and deletion

    def test_profile_is_saved_correctly(self, profile_1, user_1):
        test_profile = PersonalProfile.objects.filter(user=user_1).first()
        assert test_profile.company == profile_1.company
        assert test_profile.user == profile_1.user
        assert test_profile.about == profile_1.about
        assert test_profile.birth_date == profile_1.birth_date
        assert test_profile.profile_pic == profile_1.profile_pic
        assert test_profile.resume == profile_1.resume

    def test_profile_is_deleted(self, user_1):
        test_profile = PersonalProfile.objects.filter(user=user_1).first()
        assert test_profile in PersonalProfile.objects.all()
        test_profile.delete()
        assert test_profile not in PersonalProfile.objects.all()


@pytest.mark.django_db
class TestProfileUserRelation:
    # Testing personal profile model and user relation

    def test_profile_is_deleted_when_user_is_deleted(self, user_1):
        test_profile = PersonalProfile.objects.filter(user=user_1).first()
        test_user = User.objects.filter(password='userpassword').first()
        test_user.delete()
        assert test_profile not in PersonalProfile.objects.all()
