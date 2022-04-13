from django.shortcuts import render


def job_board(request):
    context = {'title': 'Job Board'}
    return render(request, 'job_board/job_board.html', context)
