from django.db import models
from .job_type import JobType
from .location import Location


class Preference(models.Model):

    class yearsOfExperience(models.TextChoices):
        NOEXPERIENCE = "no experience", "no experience"
        YEARS0TO2 = "0-2 years", "0-2 years"
        YEARS3TO5 = "3-5 years", "3-5 years"
        YEARS5ANDABOVE = "5+ years", "5+ years"

    class workSchedule(models.TextChoices):
        NOTSPECIFIED = "Not specified", "Not specified"
        FULLTIME = "Full-time", "Full-time"
        PARTTIME = "Part-time", "Part-time"
        FLEXIBLE = "Flexible", "Flexible"

    job_type = models.ForeignKey(JobType, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    years_of_experience = models.CharField(
        max_length=30,
        choices=yearsOfExperience.choices,
        default=yearsOfExperience.NOEXPERIENCE
    )
    work_schedule = models.CharField(
        max_length=30,
        choices=workSchedule.choices,
        default=workSchedule.NOTSPECIFIED
    )

    def __str__(self):
        return str(self.id)
