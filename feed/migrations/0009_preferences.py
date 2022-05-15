from django.db import migrations
from job_board.models.preference import Preference, JobType, Location
from feed.resources.preferences import PREFERENCES
from job_board.resources.locations import LOCATIONS


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_users'),
        ('job_board', '0004_preference_work_schedule_and_more'),
    ]

    def generate_preferences(apps, schema_editor):
        LOCATIONS.sort()
        for city in LOCATIONS:
            Preference.objects.create(
                job_type=JobType.objects.first(),
                location=Location.objects.filter(name=city[0]).first(),
                years_of_experience=Preference.yearsOfExperience.NOTSPECIFIED,
                work_schedule=Preference.workSchedule.NOTSPECIFIED
            )

        for preference in PREFERENCES:
            Preference.objects.create(
                job_type=JobType.objects.filter(text=preference[0]).first(),
                location=Location.objects.filter(name=preference[1]).first(),
                years_of_experience=preference[2],
                work_schedule=preference[3]
            ).save()

    operations = [
        migrations.RunPython(generate_preferences),
    ]
