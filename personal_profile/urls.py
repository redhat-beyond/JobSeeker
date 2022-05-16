from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('update_profile/', views.updateProfile, name='update_profile')
]
