from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                    'class': 'form-control mb-3',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Content',
                    'class': 'form-control mb-3',
                }
            ),
        }
