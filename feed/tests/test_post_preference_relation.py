import pytest
from feed.models import Post
from job_board.models.preference import Preference, JobType, Location, YearsOfExperience
import django.contrib.auth


User = django.contrib.auth.get_user_model()
POST_TITLE = "Some First Post Title"
POST_CONTENT = "Some first post content here"


@pytest.fixture
def users(db):
    user0 = User.objects.create_user('user1', password='pass123')
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
            job_type=JobType.objects.first(),
            location=Location.objects.first(),
            years_of_experience=YearsOfExperience.objects.first()).first()
        post = Post.posts.filter(content=POST_CONTENT).first()
        assert post in Post.posts.main_feed()
        assert preference in Preference.objects.all()
        preference.delete()
        assert post in Post.posts.main_feed()
