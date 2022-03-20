from django.shortcuts import render


def chat_fullscreen(request):
    return render(request, 'chat_fullscreen.html')
