import pytest
from django.db.models.query import QuerySet
from feed.models import Post
import django.contrib.auth
User = django.contrib.auth.get_user_model()


@pytest.fixture
@pytest.mark.django_db
def posts():
    POSTS = [
        (
            'Im Job Seeking!',
            'Looking for a librarian opportunity',
            User.objects.get(username='John Doe').id
        ),
        (
            'Please help me find a job',
            'Looking for a Graphic Designer opportunity',
            User.objects.get(username='Jane Doe').id
        ),
        (
            'I am looking for a job!',
            'Looking for an electrician position',
            User.objects.get(username='John Doe').id
        ),
        (
            'Im a Job Seeker!',
            'Looking for a secretary full time position',
            User.objects.get(username='Jane Doe').id
        ),
        (
            'Im Job Seeking!',
            'Looking for a django web developing opportunity',
            User.objects.get(username='Jane Doe').id
        ),
        (
            'Im a Job Seeker!',
            'Looking for a delivery driver opportunity',
            User.objects.get(username='John Doe').id
        ),
        (
            'Apple Is Hiring!',
            'We are looking for a talented human resources specialist to work at our Tel Aviv office',
            User.objects.get(username='Tim Cook').id
        ),
        (
            'Microsoft Is Hiring!',
            'We are looking for an accountant to work at our Tel Aviv office',
            User.objects.get(username='Bill Gates').id
        ),
        (
            'Apple Is Hiring!',
            'We are looking for a database administrator to work at our Tel Aviv office',
            User.objects.get(username='Tim Cook').id
        ),
        (
            'Microsoft Is Hiring!',
            'We are looking for a graphic designer to work at our Herzliya offices',
            User.objects.get(username='Bill Gates').id
        ),
        (
            'Apple Is Hiring!',
            'We are looking for a web developer to work at our Tel Aviv office',
            User.objects.get(username='Tim Cook').id
        ),
        (
            'Microsoft Is Hiring!',
            'We are looking for a delivry driver to work at our Haifa office',
            User.objects.get(username='Bill Gates').id
        ),
    ]

    return POSTS


@pytest.mark.django_db
class TestFeedPosts:
    def test_main_feed(cls, posts):
        feed = Post.posts.main_feed()
        assert isinstance(feed, QuerySet)
        assert all(isinstance(post, Post) for post in feed)
        for post in posts:
            assert post in feed.values_list('title', 'content', 'author')
