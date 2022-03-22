from django.contrib import admin
from job_board.models.job_type import JobType
from job_board.models.location import Location
from job_board.models.preference import Preference
from job_board.models.years_of_experience import YearsOfExperience


admin.site.register(Location)
admin.site.register(JobType)
admin.site.register(YearsOfExperience)
admin.site.register(Preference)
