import pytest
from .models import Post, Comment
from job_board.models.preference import Preference, JobType, Location, YearsOfExperience
import django.contrib.auth


User = django.contrib.auth.get_user_model()
POST_TITLE = "Some First Post Title"
POST_CONTENT = "Some first post content here"


@pytest.fixture
def users(db):
    user0 = User.objects.create_user('John Doe', password='pass123')
    user1 = User.objects.create_user('Jane Doe', password='pass321')
    return [user0, user1]


@pytest.fixture
def post0(db, users):
    return Post.posts.create(title=POST_TITLE, content=POST_CONTENT, author=users[0])


@pytest.mark.django_db
class TestPostModel:
    # Testing different post attributes

    def test_new_post(self, users, post0):
        # Testing post data
        assert post0.title == POST_TITLE
        assert post0.content == POST_CONTENT
        assert post0.author == users[0]

    def test_post_save(self, post0):
        # Testing post save in DB
        post0.save()
        assert post0 in Post.posts.main_feed()

    def test_post_like(self, users, post0):
        # Testing likes DB
        post0.save()
        post0.likes.add(users[1])
        assert users[1] in post0.likes.all()

    def test_unlike(self, users, post0):
        # Testing unlike
        post0.save()
        post0.likes.add(users[1])
        assert users[1] in post0.likes.all()
        post0.likes.remove(users[1])
        assert users[1] not in post0.likes.all()

    def test_post_delete(self, post0):
        # Testing removal of a post
        post0.save()
        assert post0 in Post.posts.main_feed()
        post0.delete()
        assert post0 not in Post.posts.main_feed()


@pytest.fixture
def liked_post0(post0, users):
    post0.save()
    post0.likes.add(users[1])
    return post0


@pytest.mark.django_db
class TestPostUserRelation:
    # Testing post model and user relation

    def test_remove_like_user(self, liked_post0, users):
        # Testing if removal of user also removes the like
        # In this case, users[1] have liked post0
        assert users[1] in liked_post0.likes.all()
        users[1].delete()
        assert users[1] not in liked_post0.likes.all()

    def test_remove_author(self, post0, users):
        # Testing if removing the author also removes the post
        # In this case users[0] is the author of post0
        post0.save()
        assert post0.author == users[0]
        assert post0 in Post.posts.main_feed()
        users[0].delete()
        assert post0 not in Post.posts.main_feed()


@pytest.fixture
def post_with_preferences(db, users):
    preferences0 = Preference.objects.create(
        job_type=JobType.objects.first(),
        location=Location.objects.first(),
        years_of_experience=YearsOfExperience.objects.first())
    post = Post.posts.create(
        title=POST_TITLE,
        content=POST_CONTENT,
        author=users[0],
        is_job_offer=True,
        prefernces=preferences0)

    return [post, preferences0]


@pytest.mark.django_db
class TestPostPreferencesRelation:
    # Testing post model and preference model relation

    def test_post_prefernces_removal(self, users, post_with_preferences):
        # Testing that a preference removal doesn't removes the post
        # In this case post_with_preferences[1] is the preference of post post_with_preferences[0]
        preference = post_with_preferences[1]
        post = post_with_preferences[0]
        preference.save()
        post.save()
        assert post in Post.posts.main_feed()
        assert preference in Preference.objects.all()
        preference.delete()
        assert post in Post.posts.main_feed()


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

    def test_new_comment(self, comments, users, post0):
        # Testing comment data
        assert comments[0].author == users[1]
        assert comments[0].post_parent == post0
        assert comments[0].content == COMMENT1_CONTENT
        assert comments[1].comment_parent == comments[0]

    def test_comment_save(self, comments):
        # Testing comment save in DB
        comments[0].save()
        assert comments[0] in Comment.comments.all()

    def test_parent_comment_removal(self, comments):
        # Testing that removal of parent comment also removes child comment
        # In this case, comments[0] is the parent of comment[1]
        comments[0].save()
        comments[1].save()
        assert comments[0] in Comment.comments.all()
        assert comments[1] in Comment.comments.all()
        comments[0].delete()
        assert comments[0] not in Comment.comments.all()
        assert comments[1] not in Comment.comments.all()

    def test_child_comment_removal(self, comments):
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

    def test_comment_author_removal(self, users, comments):
        # Testing that an author removal also removes the comment
        # In this case the author of comments[0] is users[1]
        comments[0].save()
        users[1].delete()
        assert comments[0] not in Comment.comments.all()

    def test_removing_comment_to_author(self, users, comments):
        # Testing that a comment removal doesn't removes the author
        # In this case the author of comments[0] is users[1]
        comments[0].save()
        assert comments[0] in Comment.comments.all()
        comments[0].delete()
        assert users[1] in User.objects.all()


@pytest.mark.django_db
class TestPostCommentRelation:
    # Testing post model and comment model relation

    def test_post_removal_to_comment(self, post0, comments):
        # Testing that a parent post removal also removes the comment
        # In this case the post parent of comments[0] is post0
        post0.save()
        comments[0].save()
        post0.delete()
        assert post0 not in Post.posts.main_feed()
        assert comments[0] not in Comment.comments.all()

    def test_comment_removal_to_post(self, post0, comments):
        # Testing that a comment removal doesn't also removes the parent post
        # In this case the post parent of comments[0] is post0
        post0.save()
        comments[0].save()
        comments[0].delete()
        assert comments[0] not in Comment.comments.all()
        assert post0 in Post.posts.main_feed()
