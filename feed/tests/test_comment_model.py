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
def post0(db, users):
    post = Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=users[0])
    post.save()
    return post


COMMENT1_CONTENT = "Some first comment content goes here"
COMMENT2_CONTENT = "Some second comment content goes here"


@pytest.fixture
def comments(post0, users):
    comment0 = Comment(author=users[1], post_parent=post0, content=COMMENT1_CONTENT)
    comment0.save()
    comment1 = Comment(author=users[0], post_parent=post0, comment_parent=comment0, content=COMMENT2_CONTENT)
    comment1.save()
    return [comment0, comment1]


@pytest.mark.django_db
class TestCommentModel:
    # Testing different comment attributes

    def test_new_comment_properties(self, comments, users, post0):
        # Testing comment data
        comment = Comment.comments.filter(content=comments[0].content).first()
        assert comment.author == comments[0].author
        assert comment.post_parent == comments[0].post_parent
        assert comment.content == comments[0].content
        assert comment.comment_parent == comments[0].comment_parent

    def test_comment_save_to_db(self, comments):
        # Testing comment save in DB
        comment = Comment.comments.filter(content=comments[0].content).first()
        assert comment in Comment.comments.all()

    def test_parent_comment_removal_to_child_comment(self, comments):
        # Testing that removal of parent comment also removes child comment
        # In this case, comments[0] is the parent of comment[1]
        comment0 = Comment.comments.filter(content=comments[0].content).first()
        comment1 = Comment.comments.filter(content=comments[1].content).first()
        assert comment0 in Comment.comments.all()
        assert comment1 in Comment.comments.all()
        comment0.delete()
        assert comment0 not in Comment.comments.all()
        assert comment1 not in Comment.comments.all()

    def test_child_comment_removal_to_parent_comment(self, comments):
        # Testing that removal of child comment doesn't removes parent comment
        # In this case, comments[0] is the parent of comment[1]
        comment0 = Comment.comments.filter(content=comments[0].content).first()
        comment1 = Comment.comments.filter(content=comments[1].content).first()
        assert comment0 in Comment.comments.all()
        assert comment1 in Comment.comments.all()
        comment1.delete()
        assert comment1 not in Comment.comments.all()
        assert comment0 in Comment.comments.all()


@pytest.mark.django_db
class TestCommentUserRelation:
    # Testing comment model and user relation

    def test_author_removal_to_post(self, users, comments):
        # Testing that an author removal also removes the comment
        # In this case the author of comments[0] is users[1]
        comment = Comment.comments.filter(content=comments[0].content).first()
        author = User.objects.filter(username=users[1].username).first()
        author.delete()
        assert comment not in Comment.comments.all()

    def test_comment_removal_to_author(self, users, comments):
        # Testing that a comment removal doesn't removes the author
        # In this case the author of comments[0] is users[1]
        comment = Comment.comments.filter(content=comments[0].content).first()
        assert comment in Comment.comments.all()
        comment.delete()
        author = User.objects.filter(username=users[1].username).first()
        assert author in User.objects.all()
