import pytest
from django.db.models.query import QuerySet
from feed.models import Post
import django.contrib.auth
User = django.contrib.auth.get_user_model()


@pytest.mark.django_db
class TestFeedPosts:
    def test_main_feed(cls):
        feed = Post.posts.main_feed()
        assert isinstance(feed, QuerySet)
        assert all(isinstance(post, Post) for post in feed)
        assert list(feed.values_list('title', 'content', 'author')) == [
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
                'We are looking for a web developer to work at our Tel Aviv office',
                User.objects.get(username='Tim Cook').id
            ),
            (
                'Microsoft Is Hiring!',
                'We are looking for a delivry driver to work at our Haifa office',
                User.objects.get(username='Bill Gates').id
            ),
        ]
