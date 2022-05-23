from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from personal_profile.forms import ProfileForm
from .models import PersonalProfile
from django.shortcuts import render


class ProfileDetailView(DetailView):
    model = PersonalProfile

class ProfileUpdateView(UpdateView):
     model = PersonalProfile
     form_class= ProfileForm
     template_name = 'profile_update_form.html'