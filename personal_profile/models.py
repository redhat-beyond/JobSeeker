# from tkinter.tix import Tree
import os
from django.db import models
from django.contrib.auth.models import User
from app.settings import MEDIA_ROOT


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

    def delete(self):

        # Get the media root path, and remove the first `/vagrant` folder.
        media_root_path = os.path.join(*(MEDIA_ROOT.split(os.path.sep)[2:]))

        file_paths_to_delete = [media_root_path + "/" + self.profile_pic.name,
                                media_root_path + "/" + self.resume.name]

        # Filter list.
        file_paths_to_delete = [i for i in file_paths_to_delete if
                                i is not None]

        # Delete files from the backend.
        if file_paths_to_delete:
            for file_path in file_paths_to_delete:
                print(f'deleting {file_path}')
                os.remove(file_path, dir_fd=None)

        # Call Django's ORM delete this record.
        super(PersonalProfile, self).delete()

    def __str__(self):
        return f'{self.user.username} Profile'
