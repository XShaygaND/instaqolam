from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm, CommentForm


class PostListView(ListView):
    """Basic ListView for Post model which is order by first pub_date and then pk"""
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-pub_date', '-pk']


def PostLikeView(request, pk):
    """A function-based view for liking a post, won't work if the user isn't authenticated"""
    post = get_object_or_404(Post, unique_id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('details', args=[str(pk)]))


def PostCommentView(request, pk):
    """A function-based view for commentin on a post, won't work if the user isn't authenticated"""

    print(request.POST)
    post = get_object_or_404(Post, unique_id=request.POST.get('blogpost_id'))
    data = request.POST.copy()
    if request.method == 'POST':
        comment_form = CommentForm(data=data)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    print(data)

    return HttpResponseRedirect(reverse('details', args=[str(pk)]))


class PostDetailView(DetailView):
    """Basic DetailView for Post model, the amount of likes are added to the context in get_context_data
    User authorization is required to see the like button and the comment section, if not authenticated, nothing will be shown instead"""

    model = Post
    template_name = 'posts/details.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, unique_id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True

        data['number_of_likes'] = likes_connected.number_of_likes() # Adding number of likes to the context so it will be shown on the template
        data['post_is_liked'] = liked # Adding status of the post being liked by the user to the context
        return data


class PostCreateView(LoginRequiredMixin, CreateView):
    """Basic CreateView for Post model which requires user authentication(LoginRequiredMixin)"""

    login_url = 'login' # Change to ur preferable login url name
    model = Post
    form_class = PostForm
    template_name = "posts/new_post.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user # Setting the post author to the request user
        self.object.save()
        form.save_m2m() # Required for django-taggit to save the tags
        return HttpResponseRedirect(self.get_success_url())


class PostUpdateView(UpdateView):
    """Basic UpdateView for Post model which requires user authentication and the request user must be the same as the post autor"""

    model = Post
    form_class = PostForm
    template_name = "posts/update_post.html"

    def dispatch(self, request, *args, **kwargs):
        """Checks if the request user is authenticated and is also the author if the post"""

        post = self.get_object()
        if request.user.is_authenticated and post.author == self.request.user:
            return super(PostUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(post) # Redirect to post's details page (Post model's get_absolute_url)

    def get_success_url(self):
        return reverse_lazy('details', args=(self.object.pk,)) # Redirect to post's details page after success


class PostDeleteView(DeleteView):
    """Basic DeleteView for Post model which requires user authentication and the request user must be the same as the post autor"""

    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        """Checks if the request user is authenticated and is also the author if the post"""
        post = self.get_object()
        if request.user.is_authenticated and post.author == self.request.user:
            return super(PostDeleteView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(post) # Redirect to post's details page (Post model's get_absolute_url)
        
    def get_success_url(self):
        return reverse_lazy('details', args=(self.object.pk,)) # Redirect to post's details page after success


class PostTagListView(ListView):
    """Basic ListView for Post's with a certaing tag"""
    model = Post
    template_name = "posts/tag_view.html"
    ordering = ['-pub_date', '-pk']

    def get_queryset(self):
        queryset = super(PostTagListView, self).get_queryset()
        tag = self.kwargs['tag']
        print(tag)
        queryset = queryset.filter(tags__name=tag).distinct() # Filter posts with the tag in URL's parameter
        return queryset
