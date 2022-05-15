import pytest
from feed.models import Post
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from feed.forms import PostForm


USERNAME1 = 'username1'
USERNAME2 = 'username2'
USER_PASS = 'secret_pass'
POST_TITLE = 'post title'
POST_CONTENT = 'some post content'
LOGIN_URL = '/login/'
POST_DETAIL_URL = '/post/'
FEED_URL = '/'
NEW_POST_URL = '/post/new/'
LOGIN_URL = '/login/'
LIKE_WARNING_MESSAGE = 'You must login in order to like a post'
REDIRECT_URL_STATUS = 302
PAGE_NOT_FOUND = 404


def post_delete_url(post_id):
    return f"/post/{post_id}/delete/"


def post_like_url(post_id):
    return f"/post/{post_id}/like/"


@pytest.fixture
def users(db):
    user1 = User.objects.create_user(USERNAME1, password=USER_PASS)
    user2 = User.objects.create_user(USERNAME2, password=USER_PASS)
    return [user1, user2]


@pytest.fixture
def logged_in_client(client, users):
    client.force_login(users[0])
    return client


@pytest.fixture
def post(db, users):
    post = Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=users[0])
    post.save()
    return post


@pytest.fixture
def initial_posts_no(db):
    return Post.posts.count()


@pytest.fixture
def liked_post(post, users):
    post.likes.add(users[0])
    return post


@pytest.fixture
def post_init_like_count(post):
    return post.likes.count()


@pytest.fixture
def liked_post_init_like_count(liked_post):
    return liked_post.likes.count()


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


class TestPostDeleteView:
    def test_delete_url_for_logged_out_user(self, post, client):
        # Testing to verify that when logged out user tryies to delete a post
        # the user gets a 302 response code and that the post remains
        post_to_delete = Post.posts.filter(title=post.title, content=post.content, author=post.author).first()
        response = client.get(post_delete_url(post_to_delete.id))
        assert response.status_code == 302
        assert post_to_delete in Post.posts.all()

    def test_delete_url_for_non_author_user(self, request, client, post):
        # Testing that if a logged in, non author, user tries to delete
        # a post, a 403 response will return
        post_to_delete = Post.posts.filter(title=post.title, content=post.content, author=post.author).first()
        non_author_user = authenticate(request, username=USERNAME2, password=USER_PASS)

        if non_author_user is not None:
            client.login(username=USERNAME2, password=USER_PASS)
            response = client.get(post_delete_url(post_to_delete.id))
            assert response.status_code == 403
        else:
            # The user login detail are wrong
            assert False

    def test_success_delete_using_delete_view(self, request, client, post):
        # Testing successfully deleting a post using the delete view via the delete post URL
        # Making sure the author of the post is logged in
        post_to_delete = Post.posts.filter(title=post.title, content=post.content, author=post.author).first()
        author = authenticate(request, username=USERNAME1, password=USER_PASS)
        assert post_to_delete in Post.posts.all()

        if author is not None:
            client.login(username=USERNAME1, password=USER_PASS)
            client.post(post_delete_url(post_to_delete.id))
            assert post_to_delete not in Post.posts.all()
        else:
            # The user login detail are wrong
            assert False


@pytest.mark.django_db
class TestPostCreateView:
    def test_create_new_post_view_entrypoin_auth(self, client, users):
        # Testing that for a logged in user, the new post url gets a valid response
        client.force_login(users[0])
        response = client.get(NEW_POST_URL)
        assert response.status_code == 200

    def test_create_new_post_view_entrypoint_unauth(self, client):
        # Testing that for logged out users, the create new post url
        # redirects to the login page
        response = client.get(NEW_POST_URL)
        assert response.status_code == REDIRECT_URL_STATUS
        assert response.url == LOGIN_URL + '?next=' + NEW_POST_URL

    def test_post_creation_using_form(self, users, client):
        # Testing that a post creates successfully using the create new
        # post form
        form_data = {'title': 'some title', 'content': 'some content...', }
        assert not Post.posts.filter(title=form_data['title'], content=form_data['content']).exists()
        client.force_login(users[0])
        client.post(NEW_POST_URL, form_data)
        assert Post.posts.filter(title=form_data['title'], content=form_data['content']).exists()

    def test_redirect_after_successful_post_creation(self, users, client):
        # Testing that after a successful post creation, the user gets
        # redirectd to the new post detail view page
        form_data = {'title': 'some title', 'content': 'some content...', }
        client.force_login(users[0])
        response = client.post(NEW_POST_URL, form_data)
        assert response.status_code == REDIRECT_URL_STATUS
        # The new post ID should be as the amount of posts exists
        new_post_id = Post.posts.count()
        assert response.url == POST_DETAIL_URL + str(new_post_id) + '/'


@pytest.mark.django_db
class TestPostCreatePopUpView:

    form_data = {'title': 'some title', 'content': 'some content...', }

    def test_feed_doesnt_show_form_when_logged_out(self, client):
        # Verify that for non authenticated user, a create new post form isnt
        # displayed on the feed page
        response = client.get(FEED_URL)
        assert response.status_code == 200
        template_names = set(tmpl.origin.template_name for tmpl in response.templates)
        assert 'feed/feed.html' in template_names
        assert response.context.get("form") is None

    def test_feed_show_form_when_logged_in(self, logged_in_client):
        # Verify that for an authnticated user, a create new post form
        # is displayed on the feed page
        response = logged_in_client.get(FEED_URL)
        assert response.status_code == 200
        template_names = set(tmpl.origin.template_name for tmpl in response.templates)
        assert 'feed/feed.html' in template_names
        assert isinstance(response.context.get("form"), PostForm)

    def test_post_creation_using_feed_form(self, logged_in_client, initial_posts_no):
        # Testing that a post creates successfully using the create new
        # post form
        response = logged_in_client.post(FEED_URL, self.form_data)
        assert response.status_code == REDIRECT_URL_STATUS
        assert response.url == FEED_URL
        response = logged_in_client.get(response.url)
        assert response.context['posts'].count() == initial_posts_no + 1
        template_names = set(tmpl.origin.template_name for tmpl in response.templates)
        assert 'feed/feed.html' in template_names

    def test_post_redirected_when_logged_out(self, client, initial_posts_no):
        # Testing that a post wasnt created for a non logged in user
        response = client.post(FEED_URL, self.form_data)
        assert response.status_code == REDIRECT_URL_STATUS
        assert response.url == FEED_URL
        response = client.get(response.url)
        assert response.context['posts'].count() == initial_posts_no

    def test_empty_form_is_redirected(self, logged_in_client, initial_posts_no):
        # Testing that an invalid form wont cause a creation of a new post
        response = logged_in_client.post(FEED_URL, {})
        assert response.status_code == 200
        form = response.context.get("form")
        assert isinstance(form, PostForm)
        assert not form.is_valid()
        assert response.context['posts'].count() == initial_posts_no


class TestLikeForNonLoggedUser:
    def test_like_view_return_warning_when_logged_out(self, post, client):
        # Testing that when logged out, if trying to access the like url
        # a warning message returns
        post_to_like = post
        response = client.get(post_like_url(post_to_like.id))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        assert len(messages) == 1
        assert messages[0] == LIKE_WARNING_MESSAGE

    def test_like_view_redirects_to_login_when_logged_out(self, post, client):
        # Testing that when logged out, if trying to access the like url
        # the user gets redirected to the login url
        post_to_like = post
        response = client.get(post_like_url(post_to_like.id))
        assert response.status_code == REDIRECT_URL_STATUS
        assert response.url == LOGIN_URL

    def test_like_url_doesnt_adds_like_to_post(self, post, client, post_init_like_count):
        # Testing that when logged out, if trying to access the like url
        # it doesnt adds a like to a post
        post_to_check_likes = post
        client.get(post_like_url(post_to_check_likes.id))
        assert post_to_check_likes.likes.count() == post_init_like_count


class TestLikeForLoggedUser:
    def test_like_url_adds_like_to_post(self, post, logged_in_client, post_init_like_count):
        # Testing that the like url, adds a like to a specific post
        post_to_like = post
        response = logged_in_client.get(post_like_url(post_to_like.id))
        response = logged_in_client.get(response.url)
        assert response.context['post'].id == post_to_like.id
        assert response.context['post'].likes.count() == post_init_like_count + 1

    def test_like_url_unlikes(self, liked_post, logged_in_client, liked_post_init_like_count):
        # Testing that the like url, unlike a post where the logged in
        # user have already liked the post
        post_to_unlike = liked_post
        response = logged_in_client.get(post_like_url(post_to_unlike.id))
        response = logged_in_client.get(response.url)
        assert response.status_code == 200
        assert response.context['post'].id == post_to_unlike.id
        assert response.context['post'].likes.count() == liked_post_init_like_count - 1

    def test_after_like_redirect_to_detail_view(self, post, logged_in_client):
        # Testing that after successful like, if the user got to the like URL
        # by typing it, he would get redirected to the post detail view page.
        # Also, if a user turned off the HTTP_REFERER option in his browser he would
        # get returned to the post detail view
        response = logged_in_client.get(post_like_url(post.id))
        assert response.status_code == REDIRECT_URL_STATUS
        assert response.url == POST_DETAIL_URL + f'{post.id}/'
        response = logged_in_client.get(response.url)
        assert response.status_code == 200
