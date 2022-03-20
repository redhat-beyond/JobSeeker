from django.db import models


class YearsOfExperience(models.Model):
    text = models.CharField(max_length=100)
