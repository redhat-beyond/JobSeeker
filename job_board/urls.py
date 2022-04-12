from django.urls import path
from . import views


urlpatterns = [
    path('job_board/', views.job_board, name='job_board'),
]
