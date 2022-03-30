from django.db import migrations, transaction
from personal_profile.models import PersonalProfile
from personal_profile.resources.personal_profiles import PERSONAL_PROFILES
import django.contrib.auth
from django.core.files.uploadedfile import SimpleUploadedFile
User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0005_personalprofile_resume'),
    ]

    def generate_personal_profiles(apps, schema_editor):
        with transaction.atomic():
            for profile in PERSONAL_PROFILES:
                PersonalProfile.objects.create(company=profile[0],
                                               user=User.objects.filter(username=profile[1]).first(),
                                               about=profile[2],
                                               birth_date=profile[3],
                                               profile_pic=SimpleUploadedFile(name='profile_image.jpg',
                                               content=open(profile[4], 'rb').read(), content_type='image/jpeg'),
                                               resume=SimpleUploadedFile(name='resume.jpg',
                                                                         content=open(profile[5], 'rb').read(),
                                                                         content_type='image/jpeg'),
                                                                         )


    operations = [
        migrations.RunPython(generate_personal_profiles),
    ]
