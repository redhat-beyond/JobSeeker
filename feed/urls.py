from django.urls import path
from . import views


urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
