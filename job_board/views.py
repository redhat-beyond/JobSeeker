from django.shortcuts import render


def job_board(request):
    return render(request, 'job_board/job_board.html')
