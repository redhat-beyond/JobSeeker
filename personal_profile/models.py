# from tkinter.tix import Tree
import os
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


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


@receiver(models.signals.post_delete, sender=PersonalProfile)
def auto_delete_file_on_delete(sender, instance, **kwargs):

    if instance.resume:
        if os.path.isfile(instance.resume.path):
            os.remove(instance.resume.path)

    if instance.profile_pic:
        if os.path.isfile(instance.profile_pic.path):
            os.remove(instance.profile_pic.path)


@receiver(models.signals.pre_save, sender=PersonalProfile)
def auto_delete_file_when_change(sender, instance, **kwargs):

    if not instance.pk:
        return False

    try:
        old_profile_pic = PersonalProfile.objects.get(pk=instance.pk).profile_pic
        old_resume = PersonalProfile.objects.get(pk=instance.pk).resume
    except PersonalProfile.DoesNotExist:
        return False

    new_profile_pic = instance.profile_pic
    if not old_profile_pic == new_profile_pic:
        if os.path.isfile(old_profile_pic.path):
            os.remove(old_profile_pic.path)

    new_resume = instance.resume
    if not old_resume == new_resume:
        if os.path.isfile(old_resume.path):
            os.remove(old_resume.path)
