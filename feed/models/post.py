from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .postManager import PostManager


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_job_offer = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="likes")
    posts = PostManager()

    def __str__(self):
        return self.title
