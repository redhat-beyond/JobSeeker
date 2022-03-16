from django.urls import path
from . import views


urlpatterns = [
    path('', views.personal_profile, name='personal-profile'),
]