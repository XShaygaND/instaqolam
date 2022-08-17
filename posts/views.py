from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm, PostUpdateForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Post
    form_class = PostForm
    template_name = "posts/new_post.html"

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "posts/update_post.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_authenticated and obj.author == self.request.user:
            return super(PostUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(obj)


    def get_success_url(self):         
        return reverse_lazy('details', args = (self.object.pk,))
