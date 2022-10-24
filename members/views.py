from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from posts.models import Post

from .models import Profile
from .forms import UserCreateForm, UserLoginForm, UserProfileUpdateForm, UserAccountUpdateForm, UserUsernameChangeForm, UserEmailChangeForm, UserPasswordChangeForm

User = get_user_model()


class UserCreateView(CreateView):
    """Basic CreateView for creating a new user which uses the UserCreateForm"""

    form_class = UserCreateForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy('login') # Redirect to login page if user was created

    def dispatch(self, request, *args, **kwargs):
        """Redirects user to their profile page if they are logged in, elsewise it lets the user view the page"""

        if request.user.is_anonymous:
            return super(UserCreateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(request.user.profile.slug,)))


class UserLoginView(LoginView):
    """A modified view that inherits from django.contrib.auth.views.LoginView"""
    form_class = UserLoginForm
    template_name = "auth/login.html"
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            """Redirects user to their profile page if they are logged in"""

            return super(UserLoginView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(request.user.profile.slug,)))


class UserDetailView(DetailView):
    """Basic DetailView for viewing the user's profile"""

    model = Profile
    template_name = "members/profile.html"

    def get_context_data(self, **kwargs):
        """Adds post_list to the context to be viewed on the page"""

        data = super().get_context_data(**kwargs)
        obj = self.get_object()
        data['post_list'] = Post.objects.filter(author=obj.user).order_by('-pub_date', '-pk')
        return data


class UserProfileUpdateView(UpdateView):
    """Basic UpdateView for updating user's Profile"""

    model = Profile
    form_class = UserProfileUpdateForm
    template_name = 'members/edit_profile.html'

    def dispatch(self, request, *args, **kwargs):
        """Redirects user to the profile page if the request user is unauthenticated or is not the same user as profile's user"""
        
        profile = self.get_object()
        if request.user.is_authenticated and request.user == profile.user:
            return super(UserProfileUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(profile.slug,)))

    def form_valid(self, form):
        """Sets profile's user to request user"""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UserAccountUpdateView(UpdateView):
    """Basic UpdateView for updating user's account"""

    model = User
    form_class = UserAccountUpdateForm
    template_name = 'auth/edit_account.html'
    context_object_name = 'authuser'

    def dispatch(self, request, *args, **kwargs):
        """Redirects user to the profile page if the request user is unauthenticated or is not the same user as user"""

        user = self.get_object()
        if request.user.is_authenticated and request.user == user:
            return super(UserAccountUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(user.slug,)))


class UserUsernameChangeView(UpdateView):
    """Basic UpdateView for changing the user's username"""
    model = User
    form_class = UserUsernameChangeForm
    template_name = 'auth/username.html'
    context_object_name = 'authuser'

    def dispatch(self, request, *args, **kwargs):
        """Redirects user to the profile page if the request user is unauthenticated or is not the same user as user"""

        user = self.get_object()
        if request.user.is_authenticated and request.user == user:
            return super(UserUsernameChangeView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(user.slug,)))


class UserEmailChangeView(UpdateView):
    """Basic UpdateView for changing the user's email address"""

    model = User
    form_class = UserEmailChangeForm
    template_name = 'auth/email.html'
    context_object_name = 'authuser'

    def dispatch(self, request, *args, **kwargs):
        """Redirects user to the profile page if the request user is unauthenticated or is not the same user as user"""

        user = self.get_object()
        if request.user.is_authenticated and request.user == user:
            return super(UserEmailChangeView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(user.slug,)))


class UserPasswordChangeView(UpdateView):
    """Basic UpdateView for changing the user's password"""

    model = User
    form_class = UserPasswordChangeForm
    template_name = 'auth/password.html'
    context_object_name = 'authuser'

    def get_form_kwargs(self):
        """Adds user to form kwargs so that it works with django.contrib.auth.forms.PasswordChangeForm"""
        user = self.get_object()
        kwargs = super().get_form_kwargs()
        print(kwargs)
        kwargs["user"] = user
        kwargs.pop('instance')
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        """Redirects user to the profile page if the request user is unauthenticated or is not the same user as user"""

        user = self.get_object()
        if request.user.is_authenticated and request.user == user:
            return super(UserPasswordChangeView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('profile', args=(user.slug,)))

