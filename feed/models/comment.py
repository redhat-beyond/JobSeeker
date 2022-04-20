from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .post import Post
from django.urls import reverse


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    post_parent = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    comments = models.Manager()

    def get_absolute_url(self):
        return reverse('post-detail', args=(self.post_parent.id,))
