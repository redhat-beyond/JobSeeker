import pytest
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from .models import PersonalProfile
from django.core.files.uploadedfile import SimpleUploadedFile
from pytest_django.asserts import assertTemplateUsed


GENERAL_IMAGE_PATH = '/__w/JobSeeker/JobSeeker/personal_profile/static/personal_profile/images/'
IMAGE_PATH = 'personal_profile/static/personal_profile/images/profile_pics/test_image.jpg'
PROFILE_DETAIL_URL = '/profile/'
UPDATE_PROFILE_PATH= '/update/'


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


@pytest.fixture()
def max_profile_id(db):
    return PersonalProfile.objects.all().count()


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

    def test_profile_is_deleted(self, profile_1, user_1):
        test_profile = PersonalProfile.objects.filter(user=user_1).first()
        assert test_profile in PersonalProfile.objects.all()
        test_profile.delete()
        assert test_profile not in PersonalProfile.objects.all()

    def test_check_placement_of_files(self, profile_1, user_1):
        test_profile = PersonalProfile.objects.filter(user=user_1).first()
        assert test_profile.profile_pic.path in GENERAL_IMAGE_PATH + test_profile.profile_pic.name
        assert test_profile.resume.path in GENERAL_IMAGE_PATH + test_profile.resume.name


@pytest.mark.django_db
class TestProfileUserRelation:
    # Testing personal profile model and user relation

    def test_profile_is_deleted_when_user_is_deleted(self, profile_1, user_1):
        test_profile = PersonalProfile.objects.filter(user=user_1).first()
        test_user = User.objects.filter(username='user_1').first()
        test_user.delete()
        assert test_profile not in PersonalProfile.objects.all()


@pytest.mark.django_db
class TestProfileDetailView:
    def test_detail_view_page_entrypoint(self, profile_1, user_1, client):
        # Testing to see if a valid user gets a valid detail view page
        test_user = User.objects.filter(username='user_1').first()
        client.force_login(test_user)
        response = client.get(PROFILE_DETAIL_URL + str(profile_1.id) + '/')
        assert response.status_code == 200
        assert response.context['user'] == test_user

    def test_detail_view_returned_data(self, profile_1, user_1, client):
        # Testing that the returned profile really is the one
        # that its ID has passed through the URL
        test_user = User.objects.filter(username='user_1').first()
        client.force_login(test_user)
        response = client.get(PROFILE_DETAIL_URL + str(profile_1.id) + '/')
        assert response.context['personalprofile'].id == profile_1.id

    def test_detail_view_page_for_invalid_profile_id(self, client, max_profile_id):
        # Testing to see if for an invalid profile id, the response will be 404
        # The id's start from 1 and increases by 1 for each profile, so the last profile will
        # get the id of the number of profiles, so by adding 1 we promise that it will be
        # an invalid ID
        response = client.get(PROFILE_DETAIL_URL + str(max_profile_id + 1) + '/')
        assert response.status_code == 404

    def test_detail_view_template(self, profile_1, user_1, client):
        # Testing to see if a valid user gets a valid detail view from response
        test_user = User.objects.filter(username='user_1').first()
        client.force_login(test_user)
        response = client.get(PROFILE_DETAIL_URL + str(profile_1.id) + '/')
        assertTemplateUsed(response, 'personal_profile/personalprofile_detail.html')


@pytest.mark.django_db
class TestProfileUpdateView:
    def test_update_view_profile(self, profile_1, user_1, client):
        # Testing to see if the changes made for company, birth_date and about fields
        # will result with response code of 302 
        test_profile = PersonalProfile.objects.filter(user=user_1).first()
        test_user = User.objects.filter(username='user_1').first()
        client.force_login(test_user)
        update_profile_path = PROFILE_DETAIL_URL + str(test_profile.id) + UPDATE_PROFILE_PATH
        response = client.post(update_profile_path,
            {'company': 'Update Test Company', 'birth_date': datetime.date(1992, 12, 10), 
            'about': 'Update Test About' , 'profile_pic': test_profile.profile_pic , 
            'resume': test_profile.resume})
        assert response.status_code == 302

    def test_update_view_template(self, profile_1, user_1, client):
        # Testing to see if a valid user gets a valid update view from response
        test_user = User.objects.filter(username='user_1').first()
        client.force_login(test_user)
        response = client.get(PROFILE_DETAIL_URL + str(profile_1.id) + UPDATE_PROFILE_PATH)
        assertTemplateUsed(response, 'profile_update_form.html')
