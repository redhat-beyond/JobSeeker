import pytest
from feed.models import Post
import django.contrib.auth
import random


User = django.contrib.auth.get_user_model()
POST_TITLE = "Some First Post Title"
POST_CONTENT = "Some first post content here"


def generate_random_username():
    letters = [chr(letter + ord('a')) for letter in range(0, 27)]
    return ('user_' + ''.join(random.choice(letters) for i in range(7)))


def generate_random_password():
    signs = [chr(i) for i in range(33, 123)]
    return (''.join(random.choice(signs) for i in range(10)))


@pytest.fixture
def users(db):
    user0 = User.objects.create_user(generate_random_username(), password=generate_random_password())
    user1 = User.objects.create_user(generate_random_username(), password=generate_random_password())
    return [user0, user1]


@pytest.fixture
def post_example(db, users):
    post = Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=users[0])
    post.save()
    return post


@pytest.mark.django_db
class TestPostModel:
    # Testing different post attributes

    def test_new_post(self, users, post_example):
        # Testing post data
        post = Post.posts.filter(content=post_example.content).first()
        assert post_example.title == post.title
        assert post_example.content == post.content
        assert post_example.author == post.author

    def test_post_save(self, post_example):
        # Testing post save in DB
        post = Post.posts.filter(content=post_example.content).first()
        assert post in Post.posts.main_feed()

    def test_post_like(self, users, post_example):
        # Testing likes DB
        post = Post.posts.filter(content=post_example.content).first()
        post.likes.add(users[1])
        assert users[1] in post.likes.all()

    def test_unlike(self, users, post_example):
        # Testing unlike
        post = Post.posts.filter(content=post_example.content).first()
        post.likes.add(users[1])
        assert users[1] in post.likes.all()
        post.likes.remove(users[1])
        assert users[1] not in post.likes.all()

    def test_post_delete(self, post_example):
        # Testing removal of a post
        post = Post.posts.filter(content=post_example.content).first()
        assert post in Post.posts.main_feed()
        post.delete()
        assert post not in Post.posts.main_feed()


@pytest.fixture
def liked_post_1(post_example, users):
    post_example.likes.add(users[1])
    return post_example


@pytest.mark.django_db
class TestPostUserRelation:
    # Testing post model and user relation

    def test_removal_of_user_affect_to_likes_list(self, liked_post_1, users):
        # Testing if removal of user also removes the like
        # In this case, users[1] have liked post_example
        liked_post = Post.posts.filter(content=liked_post_1.content).first()
        assert users[1] in liked_post.likes.all()
        users[1].delete()
        assert users[1] not in liked_post.likes.all()

    def test_remove_author_affect_to_post(self, post_example, users):
        # Testing if removing the author also removes the post
        # In this case users[0] is the author of post_example
        post = Post.posts.filter(content=post_example.content).first()
        assert post.author == users[0]
        assert post in Post.posts.main_feed()
        users[0].delete()
        assert post not in Post.posts.main_feed()
