import django.contrib.auth
from feed.tests.test_post_model import generate_random_password, generate_random_username
from feed.models import Post
from job_board.models.job_type import JobType
from job_board.models.location import Location
from job_board.models.preference import Preference
from job_board.search_engine import SearchEngine
import pytest


POST_TITLE = "Some First Post Title"
POST_CONTENT = "Some first post content here"
CITIES = ["Haifa", "Tel Aviv", "Jerusalem", "Be'er Sheva"]
User = django.contrib.auth.get_user_model()


@pytest.mark.django_db
@pytest.fixture
def create_user(db):
    return User.objects.create_user(generate_random_username(), password=generate_random_password())


@pytest.mark.django_db
@pytest.fixture
def create_search_preferences(db):

    preferences = []
    for city in CITIES:
        preferences.append(
            Preference.objects.create(
                job_type=JobType.objects.filter(text="Web developer").first(),
                location=Location.objects.filter(name=city).first(),
                years_of_experience=Preference.yearsOfExperience.NOTSPECIFIED,
                work_schedule=Preference.workSchedule.NOTSPECIFIED)
        )

    return preferences


@pytest.mark.django_db
@pytest.fixture
def create_posts(db, create_user, create_search_preferences):

    posts = []
    user = create_user
    for preference in create_search_preferences:
        posts.append(
            Post.posts.create(
                title=POST_TITLE,
                content=POST_CONTENT,
                author=user,
                is_job_offer=True,
                prefernces=preference)
        )

    return posts


class TestSearchEngineLocationOrder:

    def test_search_location_order(self, create_posts, create_search_preferences):
        post_Haifa = create_posts[0]
        post_TelAviv = create_posts[1]
        post_Jerusalem = create_posts[2]
        post_BeerSheva = create_posts[3]
        preference_Haifa = create_search_preferences[0]
        preference_TelAviv = create_search_preferences[1]
        preference_Jerusalem = create_search_preferences[2]
        preference_BeerSheva = create_search_preferences[3]

        # Haifa
        posts = SearchEngine.search(preference_Haifa)
        assert posts.index(post_Haifa) < posts.index(post_TelAviv) < \
            posts.index(post_Jerusalem) < posts.index(post_BeerSheva)

        # TelAviv
        posts = SearchEngine.search(preference_TelAviv)
        assert posts.index(post_TelAviv) < posts.index(post_Jerusalem) < \
            posts.index(post_Haifa) < posts.index(post_BeerSheva)

        # Jerusalem
        posts = SearchEngine.search(preference_Jerusalem)
        assert posts.index(post_Jerusalem) < posts.index(post_TelAviv) < \
            posts.index(post_BeerSheva) < posts.index(post_Haifa)

        # BeerSheva
        posts = SearchEngine.search(preference_BeerSheva)
        assert posts.index(post_BeerSheva) < posts.index(post_Jerusalem) < \
            posts.index(post_TelAviv) < posts.index(post_Haifa)
