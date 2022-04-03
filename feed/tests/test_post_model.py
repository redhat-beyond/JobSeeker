import pytest
from feed.models import Post
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

    def test_removal_of_user_affect_to_likes_list(self, liked_post0, users):
        # Testing if removal of user also removes the like
        # In this case, users[1] have liked post0
        assert users[1] in liked_post0.likes.all()
        users[1].delete()
        assert users[1] not in liked_post0.likes.all()

    def test_remove_author_affect_to_post(self, post0, users):
        # Testing if removing the author also removes the post
        # In this case users[0] is the author of post0
        post0.save()
        assert post0.author == users[0]
        assert post0 in Post.posts.main_feed()
        users[0].delete()
        assert post0 not in Post.posts.main_feed()
