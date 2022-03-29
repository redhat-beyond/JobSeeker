from django.db import migrations
from feed.resources.users import USERS
import django.contrib.auth
User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_alter_comment_managers_alter_post_managers_and_more'),
    ]

    def generate_users(apps, schema_editor):
        for new_user in USERS:
            User.objects.create_user(new_user[0], password=new_user[1]).save()

    operations = [
        migrations.RunPython(generate_users),
    ]
