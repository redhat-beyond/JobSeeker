from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='update-detail')
]
