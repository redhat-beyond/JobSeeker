from django.db import models
from .job_type import JobType
from .location import Location


class Preference(models.Model):

    class yearsOfExperience(models.TextChoices):
        NOTSPECIFIED = "Not specified"
        NOEXPERIENCE = "no experience"
        YEARS0TO2 = "0-2 years"
        YEARS3TO5 = "3-5 years"
        YEARS5ANDABOVE = "5+ years"

    class workSchedule(models.TextChoices):
        NOTSPECIFIED = "Not specified"
        FULLTIME = "Full-time"
        PARTTIME = "Part-time"
        FLEXIBLE = "Flexible"

    job_type = models.ForeignKey(JobType, on_delete=models.PROTECT, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True)
    years_of_experience = models.CharField(
        max_length=30,
        choices=yearsOfExperience.choices,
        default=yearsOfExperience.NOTSPECIFIED
    )
    work_schedule = models.CharField(
        max_length=30,
        choices=workSchedule.choices,
        default=workSchedule.NOTSPECIFIED
    )

    def __str__(self):
        return str(self.id)
