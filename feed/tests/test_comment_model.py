import pytest
from feed.models import Post, Comment
import django.contrib.auth


User = django.contrib.auth.get_user_model()
POST_TITLE = "Some First Post Title"
POST_CONTENT = "Some first post content here"


@pytest.fixture
def users(db):
    user0 = User.objects.create_user('user1', password='pass123')
    user1 = User.objects.create_user('user2', password='pass321')
    return [user0, user1]


@pytest.fixture
def post0(db, users):
    return Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=users[0])


COMMENT1_CONTENT = "Some first comment content goes here"
COMMENT2_CONTENT = "Some second comment content goes here"


@pytest.fixture
def comments(post0, users):
    comment0 = Comment(author=users[1], post_parent=post0, content=COMMENT1_CONTENT)
    comment1 = Comment(author=users[0], post_parent=post0, comment_parent=comment0, content=COMMENT2_CONTENT)
    return [comment0, comment1]


@pytest.mark.django_db
class TestCommentModel:
    # Testing different comment attributes

    def test_new_comment_properties(self, comments, users, post0):
        # Testing comment data
        assert comments[0].author == users[1]
        assert comments[0].post_parent == post0
        assert comments[0].content == COMMENT1_CONTENT
        assert comments[1].comment_parent == comments[0]

    def test_comment_save_to_db(self, comments):
        # Testing comment save in DB
        comments[0].save()
        assert comments[0] in Comment.comments.all()

    def test_parent_comment_removal_to_child_comment(self, comments):
        # Testing that removal of parent comment also removes child comment
        # In this case, comments[0] is the parent of comment[1]
        comments[0].save()
        comments[1].save()
        assert comments[0] in Comment.comments.all()
        assert comments[1] in Comment.comments.all()
        comments[0].delete()
        assert comments[0] not in Comment.comments.all()
        assert comments[1] not in Comment.comments.all()

    def test_child_comment_removal_to_parent_comment(self, comments):
        # Testing that removal of child comment doesn't removes parent comment
        # In this case, comments[0] is the parent of comment[1]
        comments[0].save()
        comments[1].save()
        assert comments[0] in Comment.comments.all()
        assert comments[1] in Comment.comments.all()
        comments[1].delete()
        assert comments[1] not in Comment.comments.all()
        assert comments[0] in Comment.comments.all()


@pytest.mark.django_db
class TestCommentUserRelation:
    # Testing comment model and user relation

    def test_author_removal_to_post(self, users, comments):
        # Testing that an author removal also removes the comment
        # In this case the author of comments[0] is users[1]
        comments[0].save()
        users[1].delete()
        assert comments[0] not in Comment.comments.all()

    def test_comment_removal_to_author(self, users, comments):
        # Testing that a comment removal doesn't removes the author
        # In this case the author of comments[0] is users[1]
        comments[0].save()
        assert comments[0] in Comment.comments.all()
        comments[0].delete()
        assert users[1] in User.objects.all()
