from django.db import models


class JobType(models.Model):
    text = models.CharField(max_length=100)
