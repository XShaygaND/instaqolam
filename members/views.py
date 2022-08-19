from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import UserCreateForm, UserLoginForm

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "auth/login.html"
    success_url = reverse_lazy('index')

