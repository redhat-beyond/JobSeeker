from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def main_feed(self):
        return self.order_by('-date_posted')


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


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    post_parent = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    comments = models.Manager()
