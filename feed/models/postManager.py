from django.db import models


class PostManager(models.Manager):
    def main_feed(self):
        return self.order_by('-date_posted')
