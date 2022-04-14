from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView


def feed(request):
    context = {
        'posts': Post.posts.main_feed(),
        'title': 'Feed'
    }
    return render(request, 'feed/feed.html', context)


class PostDetailView(DetailView):
    model = Post
