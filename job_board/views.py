from django.shortcuts import render
from django.views.generic.edit import FormView
from .search_form import SearchForm
from .search_engine import SearchEngine


class AddSearchView(FormView):

    template_name = 'job_board/job_board.html'
    form_class = SearchForm
    success_url = '/job_board/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Job Board'
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'title': 'Job Board', 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            posts = SearchEngine.search(self, form.save(commit=False))
            context = {'title': 'Job Board', 'results': posts, 'form': form}
        else:
            context = {'title': 'Job Board', 'form': form}

        return render(request, self.template_name, context)
