import pytest
from feed.models import Post
from job_board.models.preference import Preference, JobType, Location, YearsOfExperience
import django.contrib.auth
import random


User = django.contrib.auth.get_user_model()
POST_TITLE = "Some First Post Title"
POST_CONTENT = "Some first post content here"


def generate_random_username():
    letters = [chr(l + ord('a')) for l in range(0,27)]
    return ( 'user_' + ''.join(random.choice(letters) for i in range(7)))


def generate_random_password():
    signs = [chr(i) for i in range(33,123)]
    return ( ''.join(random.choice(signs) for i in range(10)))


@pytest.fixture
def users(db):
    user0 = User.objects.create_user(generate_random_username(), password=generate_random_password())
    return [user0]


@pytest.fixture
def post_with_preferences(db, users):
    preferences0 = Preference.objects.create(
        job_type=JobType.objects.first(),
        location=Location.objects.first(),
        years_of_experience=YearsOfExperience.objects.first())
    post = Post.posts.create(
        title=POST_TITLE,
        content=POST_CONTENT,
        author=users[0],
        is_job_offer=True,
        prefernces=preferences0)

    preferences0.save()
    post.save()
    return [post, preferences0]


@pytest.mark.django_db
class TestPostPreferencesRelation:
    # Testing post model and preference model relation

    def test_prefernces_removal_to_post(self, users, post_with_preferences):
        # Testing that a preference removal doesn't removes the post
        # In this case post_with_preferences[1] is the preference of post post_with_preferences[0]
        preference = Preference.objects.filter(
            job_type=post_with_preferences[0].prefernces.job_type,
            location=post_with_preferences[0].prefernces.location,
            years_of_experience=post_with_preferences[0].prefernces.years_of_experience).first()
        post = Post.posts.filter(content=post_with_preferences[0].content).first()
        assert post in Post.posts.main_feed()
        assert preference in Preference.objects.all()
        preference.delete()
        assert post in Post.posts.main_feed()
