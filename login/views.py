from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required  # to be changed
def profile(request):
    return render(request, 'login.html')
