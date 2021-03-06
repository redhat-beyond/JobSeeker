from django.urls import path
from . import views


urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/like/', views.LikeView, name='like-post'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
