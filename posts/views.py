from django.shortcuts import render

from django.views.generic import ListView

from .models import Post


class IndexView(ListView):
    model = Post
    template_name = 'posts/index.html'
