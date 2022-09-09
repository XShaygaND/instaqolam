from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from posts.models import Post

from .models import Profile
from .forms import UserCreateForm, UserLoginForm, UserProfileUpdateForm


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super(UserCreateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(request.user.profile.slug,)))


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "auth/login.html"
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return super(UserLoginView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(request.user.profile.slug,)))


class UserDetailView(DetailView):
    model = Profile
    template_name = "members/profile.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        obj = self.get_object()
        data['post_list'] = Post.objects.filter(author=obj.user)
        return data


class UserProfileUpdateView(UpdateView):
    model = Profile
    form_class = UserProfileUpdateForm
    template_name = 'members/edit_profile.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        profile = self.get_object()
        if request.user.is_authenticated and request.user == profile.user:
            return super(UserProfileUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(profile.slug,)))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())