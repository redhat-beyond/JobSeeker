from django.db import migrations
from feed.models import Post, Comment
from feed.resources.comments import COMMENTS
import django.contrib.auth
User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0010_posts'),
    ]

    def generate_comments(apps, schema_editor):
        for comment in COMMENTS:
            Comment.comments.create(
                author=User.objects.filter(username=comment[0]).first(),
                comment_parent=None if comment[1] is None else Comment.comments.filter(content=comment[1]).first(),
                post_parent=Post.posts.filter(title=comment[2]).first(),
                content=comment[3],
            ).save()

    operations = [
        migrations.RunPython(generate_comments),
    ]
