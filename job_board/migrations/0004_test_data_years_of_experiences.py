from django.db import migrations
from job_board.models.years_of_experience import YearsOfExperience
from job_board.resources.years_of_experiences import YEARS_OF_EXPERIENCES


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0003_test_data_locations'),
    ]

    def generate_yearsOfExperience_data(apps, schema_editor):
        for yearsOfExperience in YEARS_OF_EXPERIENCES:
            YearsOfExperience(text=yearsOfExperience).save()

    operations = [
        migrations.RunPython(generate_yearsOfExperience_data),
    ]
