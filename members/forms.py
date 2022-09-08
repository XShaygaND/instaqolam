from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['last_name'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['email'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

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


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['profile_picture'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
