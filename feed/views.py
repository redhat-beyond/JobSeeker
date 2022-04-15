from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.views.generic import DetailView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    login_url = '/login/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    login_url = '/login/'

    def form_valid(self, form):
        post_parent_id = self.kwargs.get('pk')
        post_parent = get_object_or_404(Post, id=post_parent_id)

        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post_parent = post_parent
        comment.save()

        return super().form_valid(form)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    user = request.user
    if user.is_authenticated:
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        origin_url = request.META.get('HTTP_REFERER')
        if origin_url is not None:
            return HttpResponseRedirect(origin_url)
        return HttpResponseRedirect(reverse('post-detail', args=(str(pk),)))

    else:
        messages.warning(request, "You must login in order to like a post")
        return redirect('login')
