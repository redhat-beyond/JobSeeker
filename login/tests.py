import pytest
from django.contrib.auth.models import User


USERNAME = 'username'
USER_PASS = 'secret_pass'
LOGIN_URL = '/login/'
ABOUT_URL = '/about/'
SUCCESS_LOGIN_REDIRECT_URL = ABOUT_URL
REDIRECT_STATUS_CODE = 302
USER_CREDENTIALS = {'username': USERNAME, 'password': USER_PASS}


@pytest.fixture
def user(db):
    user = User.objects.create_user(USERNAME, password=USER_PASS)
    user.save()
    return user


class TestLogin:
    def test_login_app_entrypoint(self, client):
        response = client.get("/login/")
        assert response.status_code == 200


@pytest.mark.django_db
class TestLoginForm:
    def test_user_login_through_form_success(self, user, client):
        # Testing that the login form logs user in
        response = client.post(LOGIN_URL, USER_CREDENTIALS)
        response = client.get(response.url)
        assert response.context['user'].is_authenticated
        assert response.context['user'] == user
        # client.logout()

    def test_user_login_through_form_fail(self, user, client):
        # Testing that wrong credentials wont log in a user
        WRONG_USER_PASS = USER_PASS + '1'
        response = client.post(LOGIN_URL, {'username': USERNAME, 'password': WRONG_USER_PASS})
        assert response.status_code != REDIRECT_STATUS_CODE
        assert not response.context['user'].is_authenticated

    def test_success_login_redirects(self, user, client):
        # Testing that after successful login, the user gets redirected
        response = client.post(LOGIN_URL, USER_CREDENTIALS)
        assert response.status_code == REDIRECT_STATUS_CODE
        assert response.url == SUCCESS_LOGIN_REDIRECT_URL
