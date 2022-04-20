from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse


def feed(request):
    context = {
        'posts': Post.posts.main_feed(),
        'title': 'Feed'
    }
    return render(request, 'feed/feed.html', context)


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request, "Post deleted successfully")
        return reverse('feed')
