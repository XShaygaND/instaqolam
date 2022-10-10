from django import forms

from .models import Post

from taggit import forms as tforms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'logo', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'body': forms.Textarea(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'tags': tforms.TagWidget(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
        }
