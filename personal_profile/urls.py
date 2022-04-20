from django.urls import path
from . import views


urlpatterns = [
    path('', views.personal_profile, name='profile'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
]
