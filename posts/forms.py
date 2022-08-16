from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'body', 'author', 'logo')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'body': forms.Textarea(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'author': forms.Select(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
