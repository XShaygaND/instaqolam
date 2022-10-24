from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Profile

User = get_user_model()

class UserCreateForm(UserCreationForm):
    """A form that inherits from django.contrib.auth.forms.UserCreationForm which it's fields are bootstrapified and first and last name and email field are required"""
        
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
    """A form that inherits from django.contrib.auth.forms.AuthenticationForm which it's fields are bootstrapified"""
        
    class Meta:
        model = User
        fields = ('username', 'password')
        
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['password'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'


class UserProfileUpdateForm(forms.ModelForm):
    """A basic form for updating user profile which has bio and profile_picture fields and the fields are bootstrapified"""

    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['profile_picture'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'


class UserAccountUpdateForm(forms.ModelForm):
    """A basic form for updating user account which has first_name and last_name fields, other fields are shown in the template but not changable in this form
    Fields are bootstrapified"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserAccountUpdateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['last_name'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'

class UserUsernameChangeForm(forms.ModelForm):
    """A basic form for changing the User's username which only has a username field and the field is bootstrapified"""

    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(UserUsernameChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'


class UserEmailChangeForm(forms.ModelForm):
    """A basic form for changing the User's email address which only has an email field and the field is bootstrapified"""

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(UserEmailChangeForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'


class UserPasswordChangeForm(PasswordChangeForm):
    """A form that inherits from django.contrib.auth.forms.PasswordChangeForm which has old password and a combination of the new password and it's confirmation
    Fields are bootstrapified"""

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control bg-dark border border-secondary text-light'
