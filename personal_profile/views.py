from django.shortcuts import render

def personal_profile(request):
    return render(request, 'personal_profile/personal_profile.html')