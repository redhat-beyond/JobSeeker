from django.shortcuts import render
from django.views.generic import DetailView
from .models import PersonalProfile


def personal_profile(request):
        context = {
        'title': 'Personal Profile'
        }
        return render(request, 'personalprofile_detail.html', context)


class ProfileDetailView(DetailView):
    model = PersonalProfile
