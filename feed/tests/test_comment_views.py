import pytest
from feed.models import Post, Comment
from django.contrib.auth.models import User


USERNAME1 = 'username1'
USER_PASS = 'secret_pass'
POST_TITLE = 'post title'
POST_CONTENT = 'some post content'
LOGIN_URL = '/login/'
REDIRECT_URL_STATUS = 302
PAGE_NOT_FOUND_STATUS = 404


def new_comment_url(post_parent_id):
    return f"/post/{post_parent_id}/comment/new/"


def post_detail_view_url(post_id):
    return f"/post/{post_id}/"


@pytest.fixture
def users(db):
    user1 = User.objects.create_user(USERNAME1, password=USER_PASS)
    return [user1]


@pytest.fixture
def post(db, users):
    post = Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=users[0])
    post.save()
    return post


@pytest.fixture
def logged_in_client(client, users):
    client.force_login(users[0])
    return client


@pytest.fixture
def post_initial_comments_no(db, post):
    return Comment.comments.filter(post_parent=post).count()


@pytest.fixture
def max_post_id(db):
    return Post.posts.count()


@pytest.mark.django_db
class TestCommentCreateView:
    def test_create_new_comment_view_entrypoint_auth(self, post, logged_in_client):
        # Testing that for a logged in user, the new comment url gets a valid response
        # Also checks for the right template
        response = logged_in_client.get(new_comment_url(post.id))
        assert response.status_code == 200
        template_names = set(tmpl.origin.template_name for tmpl in response.templates)
        assert 'feed/comment_form.html' in template_names

    def test_create_new_comment_view_entrypoint_unauth(self, post, client):
        # Testing that for logged out users, the create new comment url
        # redirects to the login page
        response = client.get(new_comment_url(post.id))
        assert response.status_code == REDIRECT_URL_STATUS
        assert response.url == LOGIN_URL + '?next=' + new_comment_url(post.id)

    def test_comment_creation_using_form(self, post, logged_in_client, post_initial_comments_no):
        # Testing that a comment creates successfully using the create new
        # comment form
        form_data = {'content': 'some coment content...'}
        response = logged_in_client.post(new_comment_url(post.id), form_data)
        response = logged_in_client.get(response.url)
        assert response.context['post'].comments.count() == post_initial_comments_no + 1

    def test_redirect_after_successful_comment_creation(self, post, logged_in_client):
        # Testing that after a successful comment creation, the user gets
        # redirectd to the parent post detail view page
        form_data = {'content': 'some coment content...'}
        response = logged_in_client.post(new_comment_url(post.id), form_data)
        assert response.status_code == REDIRECT_URL_STATUS
        assert response.url == post_detail_view_url(post.id)
        response = logged_in_client.get(response.url)
        assert response.status_code == 200

    def test_404_raise_for_invalid_post_id(self, logged_in_client, max_post_id):
        # Testing that if a form with an invalid parent post id url
        # tries to get submit, a 404 raises
        form_data = {'content': 'some coment content...'}
        invalid_post_id = max_post_id + 1
        response = logged_in_client.post(new_comment_url(invalid_post_id), form_data)
        assert response.status_code == PAGE_NOT_FOUND_STATUS
