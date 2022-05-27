from django import forms
from .models import PersonalProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = PersonalProfile
        fields = ('company', 'birth_date', 'about', 'profile_pic', 'resume')
        widgets = {}
