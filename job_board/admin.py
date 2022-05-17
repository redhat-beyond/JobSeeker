from django.contrib import admin
from job_board.models.job_type import JobType
from job_board.models.location import Location
from job_board.models.preference import Preference


admin.site.register(Location)
admin.site.register(JobType)
admin.site.register(Preference)
