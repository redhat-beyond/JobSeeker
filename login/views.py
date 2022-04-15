from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required  # to be changed
def profile(request):
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)