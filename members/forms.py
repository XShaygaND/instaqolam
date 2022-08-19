from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['password1'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['password2'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['password'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
