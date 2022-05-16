from django.db import migrations
from job_board.models.location import Location
from job_board.resources.locations import LOCATIONS


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0002_test_data_job_types'),
    ]

    def generate_location_data(apps, schema_editor):
        LOCATIONS.sort()
        for location in LOCATIONS:
            Location(name=location[0], latitude=location[1], longitude=location[2]).save()

    operations = [
        migrations.RunPython(generate_location_data),
    ]
