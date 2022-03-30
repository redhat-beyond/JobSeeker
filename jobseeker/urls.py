from django.urls import path, include
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('', include('personal_profile.urls')),
    path('', include('login.urls')),
    path('', include('chat.urls')),
]
