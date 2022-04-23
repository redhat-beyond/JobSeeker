from django import forms
from job_board.models.preference import Preference


class SearchForm(forms.ModelForm):

    class Meta:
        model = Preference
        fields = ('job_type', 'location', 'years_of_experience', 'work_schedule')
