import django.contrib.auth
from feed.models import Post
from feed.tests.test_post_model import generate_random_password, generate_random_username
from job_board.models.job_type import JobType
from job_board.models.location import Location
from job_board.models.preference import Preference
from job_board.search_engine import SearchEngine
import pytest


User = django.contrib.auth.get_user_model()
POST_TITLE = "Some First Post Title"
POST_CONTENT = "Some first post content here"


@pytest.mark.django_db
@pytest.fixture
def create_user(db):
    return User.objects.create_user(generate_random_username(), password=generate_random_password())


@pytest.mark.django_db
@pytest.fixture
def create_preferences_for_posts(db):
    preference1 = Preference.objects.create(
        job_type=JobType.objects.first(),
        location=Location.objects.first(),
        years_of_experience=Preference.yearsOfExperience.YEARS5ANDABOVE,
        work_schedule=Preference.workSchedule.NOTSPECIFIED)

    preference2 = Preference.objects.create(
        job_type=JobType.objects.last(),
        location=Location.objects.first(),
        years_of_experience=Preference.yearsOfExperience.YEARS5ANDABOVE,
        work_schedule=Preference.workSchedule.NOTSPECIFIED)

    return [preference1, preference2]


@pytest.mark.django_db
@pytest.fixture
def create_posts(db, create_user, create_preferences_for_posts):
    preferences = create_preferences_for_posts
    user = create_user
    post1 = Post.posts.create(
        title=POST_TITLE,
        content=POST_CONTENT,
        author=user,
        is_job_offer=True,
        prefernces=preferences[0])
    post2 = Post.posts.create(
        title=POST_TITLE,
        content=POST_CONTENT,
        author=user,
        is_job_offer=True,
        prefernces=preferences[1])

    return [post1, post2]


@pytest.mark.django_db
@pytest.fixture
def create_search_preferences(db):
    pref1 = Preference(
        job_type=JobType.objects.first(),
        location=Location.objects.first(),
        years_of_experience=Preference.yearsOfExperience.YEARS5ANDABOVE,
        work_schedule=Preference.workSchedule.NOTSPECIFIED)

    pref2 = Preference(
        job_type=None,
        location=None,
        years_of_experience=Preference.yearsOfExperience.YEARS5ANDABOVE,
        work_schedule=Preference.workSchedule.NOTSPECIFIED)

    pref3 = Preference(
        job_type=None,
        location=None,
        years_of_experience=Preference.yearsOfExperience.NOTSPECIFIED,
        work_schedule=Preference.workSchedule.NOTSPECIFIED)

    return [pref1, pref2, pref3]


@pytest.mark.django_db
class TestSearchEngine:

    def test_find_relevant_posts_with_pref1(self, create_posts, create_search_preferences):
        post1 = create_posts[0]
        post2 = create_posts[1]
        pref1 = create_search_preferences[0]
        posts = SearchEngine.search(self, pref1)
        assert post1 in posts
        assert post2 not in posts

    def test_find_relevant_posts_with_pref2(self, create_posts, create_search_preferences):
        post1 = create_posts[0]
        post2 = create_posts[1]
        pref2 = create_search_preferences[1]
        posts = SearchEngine.search(self, pref2)
        assert post1 in posts
        assert post2 in posts

    def test_find_relevant_posts_with_pref3(self, create_posts, create_search_preferences):
        post1 = create_posts[0]
        post2 = create_posts[1]
        pref3 = create_search_preferences[2]
        posts = SearchEngine.search(self, pref3)
        assert post1 not in posts
        assert post2 not in posts
