import datetime
from django.db import migrations, transaction
from personal_profile.models import PersonalProfile
import django.contrib.auth
from django.core.files.uploadedfile import SimpleUploadedFile
User = django.contrib.auth.get_user_model()

PERSONAL_PROFILES = [
    [
        'Microsoft',
        'Bill Gates',
        'Im a co-founder of microsoft, and have been the richest guy in the world for a while...',
        datetime.date(1955, 10, 28),
        'personal_profile/static/personal_profile/images/profile_pics/image_Bill_Gates.jpg',
        'personal_profile/static/personal_profile/images/resumes/resume_Bill_Gates.jpg',
    ],
    [
        'Apple',
        'Tim Cook',
        'Im the CEO of Apple, and honestly Im just the guy everyone calls Steve Jobs',
        datetime.date(1960, 11, 1),
        'personal_profile/static/personal_profile/images/profile_pics/image_Tim_Cook.jpg',
        'personal_profile/static/personal_profile/images/resumes/resume_Tim_Cook.jpg',
    ],
    [
        'Blank',
        'John Doe',
        'Web page designing is my greates passion, django specialist and a people person',
        datetime.date(1995, 12, 10),
        'personal_profile/static/personal_profile/images/profile_pics/image_John_Doe.jpg',
        'personal_profile/static/personal_profile/images/resumes/resume_Tim_Cook.jpg',
    ],
    [
        'Blank',
        'Jane Doe',
        'Web page designing is my greates passion, django specialist and a people person',
        datetime.date(1995, 12, 10),
        'personal_profile/static/personal_profile/images/profile_pics/image_Jane_Doe.jpg',
        'personal_profile/static/personal_profile/images/resumes/resume_Tim_Cook.jpg',
    ]
]

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
                                               profile_pic=SimpleUploadedFile(name='image_' + profile[1] + '.jpg',
                                               content=open(profile[4], 'rb').read(), content_type='image/jpeg'),
                                               resume=SimpleUploadedFile(name='resume_' + profile[1] + '.jpg',
                                                                         content=open(profile[5], 'rb').read(),
                                                                         content_type='image/jpeg')).save()

    operations = [
        migrations.RunPython(generate_personal_profiles),
    ]
