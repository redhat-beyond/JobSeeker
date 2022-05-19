from django.db import migrations
from feed.models.post import Post
from job_board.models.preference import Preference, JobType
# from feed.resources.posts import POSTS
from job_board.resources.locations import LOCATIONS
import django.contrib.auth
User = django.contrib.auth.get_user_model()
import json


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_preferences'),
        ('job_board', '0004_preference_work_schedule_and_more'),
    ]

    def generate_posts(apps, schema_editor):
        # creates 1 job offer post for each location
        for i in range(1, len(LOCATIONS)):
            Post.posts.create(
                title="We are hiring",
                content="",
                author=User.objects.first(),
                is_job_offer=True,
                prefernces=Preference.objects.filter(id=i).first()
            )

        f = open('feed/resources/posts.json')
        data = json.load(f)

        for post in data['POSTS']:
            Post.posts.create(
                title=post['title'],
                content=post['content'],
                author=User.objects.filter(username=post['author']).first(),
                is_job_offer=post['is_job_offer'],
                prefernces=Preference.objects.filter(job_type=JobType.objects.filter(text=post['prefernces']).first()).first()
            ).save()

    operations = [
        migrations.RunPython(generate_posts),
    ]

