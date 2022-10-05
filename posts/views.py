from enum import unique
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-pub_date', '-pk']


def PostLikeView(request, pk):
    post = get_object_or_404(Post, unique_id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('details', args=[str(pk)]))


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, unique_id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True

        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


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
        post = self.get_object()
        if request.user.is_authenticated and post.author == self.request.user:
            return super(PostUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(post)


    def get_success_url(self):         
        return reverse_lazy('details', args=(self.object.pk,))


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
