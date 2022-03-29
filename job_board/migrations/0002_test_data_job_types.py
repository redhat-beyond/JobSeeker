from django.db import migrations
from job_board.models.job_type import JobType
from job_board.resources.job_types import JOB_TYPES


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0001_initial'),
    ]

    def generate_jobType_data(apps, schema_editor):
        for jobType in JOB_TYPES:
            JobType(text=jobType).save()

    operations = [
        migrations.RunPython(generate_jobType_data),
    ]
