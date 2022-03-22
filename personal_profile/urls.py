from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.personal_profile, name='profile'),
]
