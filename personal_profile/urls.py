from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
]
