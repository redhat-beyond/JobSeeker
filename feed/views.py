from django.shortcuts import render
from .models import Post


def feed(request):
    context = {
        'posts': Post.posts.main_feed()
    }
    return render(request, 'feed/feed.html', context)
