from django.views.generic import DetailView
from .models import PersonalProfile
from django.shortcuts import render


class ProfileDetailView(DetailView):
    model = PersonalProfile

def updateProfile(request):
    context= {}
    return render(request, 'templates/personal_profile/update_form.html')