import pytest
from feed.models import Post, Comment
from django.contrib.auth.models import User


USERNAME1 = 'username1'
USERNAME2 = 'username2'
USER_PASS = 'secret_pass'
POST_TITLE = 'post title'
POST_CONTENT = 'some post content'
COMMENT_CONTENT = 'some comment content'
LOGIN_URL = '/login/'
REDIRECT_URL_STATUS = 302
PAGE_NOT_FOUND_STATUS = 404


def new_comment_url(post_parent_id):
    return f"/post/{post_parent_id}/comment/new/"


def post_detail_view_url(post_id):
    return f"/post/{post_id}/"


def comment_delete_url(comment_id):
    return f"/comment/{comment_id}/delete/"


@pytest.fixture
def users(db):
    user1 = User.objects.create_user(USERNAME1, password=USER_PASS)
    user2 = User.objects.create_user(USERNAME2, password=USER_PASS)
    return [user1, user2]


@pytest.fixture
def post(db, users):
    post = Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=users[0])
    post.save()
    return post


@pytest.fixture
def comment(db, post, users):
    comment = Comment.comments.create(post_parent=post, content=COMMENT_CONTENT, author=users[1])
    comment.save()
    return comment


@pytest.fixture
def logged_in_client(client, users):
    client.force_login(users[0])
    return client


@pytest.fixture
def post_initial_comments_no(db, post):
    return Comment.comments.filter(post_parent=post).count()


@pytest.fixture
def initial_comment_no(db):
    return Comment.comments.count()


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


@pytest.mark.django_db
class TestCommentDeleteView:
    def test_delete_url_for_logged_out_user(self, comment, client, initial_comment_no):
        # Testing to verify that when logged out user tryies to delete a comment
        # the user gets a 302 response code and gets redirected to login page
        # Also checks for the existence of the comment
        response = client.get(comment_delete_url(comment.id))
        assert response.status_code == REDIRECT_URL_STATUS
        assert response.url == f'{LOGIN_URL}?next={comment_delete_url(comment.id)}'
        assert Comment.comments.count() == initial_comment_no

    def test_delete_url_for_non_author_user(self, logged_in_client, comment):
        # Testing that if a logged in, non author, user tries to delete
        # a comment, a 403 response will return
        response = logged_in_client.get(comment_delete_url(comment.id))
        assert response.status_code == 403

    def test_success_delete_using_delete_view(self, client, comment, users, initial_comment_no):
        # Testing successfully deleting a comment using the delete view via the delete comment URL
        # Making sure the author of the post is logged in
        client.force_login(users[1])
        client.post(comment_delete_url(comment.id))
        assert Comment.comments.count() == initial_comment_no - 1
