from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-pub_date', '-id']


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Post
    form_class = PostForm
    template_name = "posts/new_post.html"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/update_post.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_authenticated and obj.author == self.request.user:
            return super(PostUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(obj)


    def get_success_url(self):         
        return reverse_lazy('details', args = (self.object.pk,))


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_authenticated and obj.author == self.request.user:
            return super(PostDeleteView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(obj)
