from django.shortcuts import render
from django.views.generic import DetailView
from .models import PersonalProfile


class ProfileDetailView(DetailView):
    model = PersonalProfile
