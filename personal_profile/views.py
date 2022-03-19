from django.shortcuts import render


def personal_profile(request):
    return render(request, 'templates/personal_profile/personal_profile.html')
