from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class ProfileManager(models.Manager):
    def main_profile(self):
        return self


class PersonalProfile(models.Model):
    company = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    birth_date = models.DateField(null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile_pics')
    resume = models.FileField(null=True, upload_to='resumes')

    def get_absolute_url(self):
        return reverse('profile-detail', args=(self.id,))
