from django.shortcuts import render
from personal_profile.models import PersonalProfile

def personal_profile(request):
    context = {
        'personal_profile': PersonalProfile
    }
    return render(request, 'personal_profile/personal_profile.html', context)