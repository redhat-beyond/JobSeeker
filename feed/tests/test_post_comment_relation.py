import pytest
from feed.models import Post, Comment
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
    user1 = User.objects.create_user(generate_random_username(), password=generate_random_password())
    return [user0, user1]


@pytest.fixture
def post_example(db, users):
    post = Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=users[0])
    post.save()
    return post


COMMENT1_CONTENT = "Some first comment content goes here"
COMMENT2_CONTENT = "Some second comment content goes here"


@pytest.fixture
def comments(post_example, users):
    comment0 = Comment(author=users[1], post_parent=post_example, content=COMMENT1_CONTENT)
    comment0.save()
    comment1 = Comment(author=users[0], post_parent=post_example, comment_parent=comment0, content=COMMENT2_CONTENT)
    comment1.save()
    return [comment0, comment1]


@pytest.mark.django_db
class TestPostCommentRelation:
    # Testing post model and comment model relation

    def test_post_removal_to_comment(self, post_example, comments):
        # Testing that a parent post removal also removes the comment
        # In this case the post parent of comments[0] is post_example
        post = Post.posts.filter(title=post_example.title, content=post_example.content).first()
        comment = Comment.comments.filter(content=comments[0].content).first()
        post.delete()
        assert post not in Post.posts.main_feed()
        assert comment not in Comment.comments.all()

    def test_comment_removal_to_post(self, post_example, comments):
        # Testing that a comment removal doesn't also removes the parent post
        # In this case the post parent of comments[0] is post_example
        post = Post.posts.filter(title=post_example.title, content=post_example.content).first()
        comment = Comment.comments.filter(content=comments[0].content).first()
        comment.delete()
        assert comment not in Comment.comments.all()
        assert post in Post.posts.main_feed()
