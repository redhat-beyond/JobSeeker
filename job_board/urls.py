from django.urls import path
from . import views


urlpatterns = [
    path('job_board/', views.AddSearchView.as_view(), name='job_board'),
]
