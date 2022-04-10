from django.urls import path
from .views import PostCreateView
from . import views


urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
