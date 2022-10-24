from django import forms

from .models import Post, Comment

from taggit import forms as tforms

class PostForm(forms.ModelForm):
    """A form for Post model which excludes the author field
    The author field will automatically be added in PostCreateView"""

    class Meta:
        model = Post
        fields = ('title', 'body', 'logo', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'body': forms.Textarea(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
            'tags': tforms.TagWidget(attrs={'class': 'form-control bg-dark border border-secondary text-light'}),
        }


class CommentForm(forms.ModelForm):
    """A form for Comment model which only has a body field
    Comment user and post fields will automatically be defined in PostCommentView"""
    
    class Meta:
        model = Comment
        fields = ('body',)
