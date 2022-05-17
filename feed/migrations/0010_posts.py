from django.db import migrations
from feed.models.post import Post
from job_board.models.preference import Preference, JobType
from feed.resources.posts import POSTS
import django.contrib.auth
User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_preferences'),
        ('job_board', '0004_preference_work_schedule_and_more'),
    ]

    def generate_posts(apps, schema_editor):
        for post in POSTS:
            Post.posts.create(
                title=post[0],
                content=post[1],
                author=User.objects.filter(username=post[2]).first(),
                is_job_offer=post[3],
                prefernces=Preference.objects.filter(job_type=JobType.objects.filter(text=post[4]).first()).first()
            ).save()

    operations = [
        migrations.RunPython(generate_posts),
    ]
