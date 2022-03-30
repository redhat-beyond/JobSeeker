from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User


class ProfileManager(models.Manager):
    def main_profile(self):
        return self


class PersonalProfile(models.Model):
    company= models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about= models.TextField() 
    birth_date= models.CharField(max_length=11, default='00/00/0000') #maybe change to date later-on 
    profile_pic= models.ImageField(null=True, blank=True)
  #  resume=
  
    def __str__(self):
      return f'{self.user.username} Profile'

