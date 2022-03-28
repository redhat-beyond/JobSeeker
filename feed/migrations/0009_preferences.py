from django.db import migrations
from job_board.models.preference import Preference, JobType, Location, YearsOfExperience
from feed.resources.preferences import PREFERENCES


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_users'),
        ('job_board', '0004_test_data_years_of_experiences'),
    ]

    def generate_preferences(apps, schema_editor):
        for preference in PREFERENCES:
            Preference.objects.create(
                job_type=JobType.objects.filter(text=preference[0]).first(),
                location=Location.objects.filter(name=preference[1]).first(),
                years_of_experience=YearsOfExperience.objects.filter(text=preference[2]).first()
            ).save()

    operations = [
        migrations.RunPython(generate_preferences),
    ]
