import pytest
from feed.models import Post
from django.contrib.auth.models import User


USERNAME = 'username'
USER_PASS = 'secret_pass'
POST_TITLE = 'post title'
POST_CONTENT = 'some post content'
POST_DETAIL_URL = '/post/'
PAGE_NOT_FOUND = 404


@pytest.fixture
def user(db):
    user = User.objects.create_user(USERNAME, password=USER_PASS)
    return user


@pytest.fixture
def post(db, user):
    post = Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=user)
    post.save()
    return post


@pytest.mark.django_db
class TestPostDetailView:
    def test_detail_view_page_entrypoint(self, post, client):
        # Testing to see if a valid post id gets a valid detail view page
        response = client.get(POST_DETAIL_URL + str(post.id) + '/')
        assert response.status_code == 200

    def test_detail_view_returned_data(self, post, client):
        # Testing that the returned post really is the one
        # that it ID has passed through the URL
        response = client.get(POST_DETAIL_URL + str(post.id) + '/')
        assert response.context['post'].id == post.id

    def test_detail_view_page_for_invalid_post_id(self, client):
        # Testing to see if for an invalid post id, the response will be 404
        # The id's start from 1 and increases by 1 for each post, so the last post will
        # get the id of the number of posts, so by adding 1 we promise that it will be
        # an invalid ID
        max_post_id = Post.posts.all().count()
        response = client.get(POST_DETAIL_URL + str(max_post_id + 1) + '/')
        assert response.status_code == PAGE_NOT_FOUND
