from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details.html'



class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/new_post.html"

