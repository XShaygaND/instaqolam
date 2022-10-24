from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from django.db import models

from .storage import OverwriteStorage

User = settings.AUTH_USER_MODEL


def get_upload_path(instance, filename):
    """Returns {instance.user.username}/profile_picture{file_extension}"""

    extension = filename.split('.')[-1]
    return f'{instance.user.username}/profile_picture.{extension}'


class User(AbstractUser):
    """Custom User model that inherits from django.contrib.auth.models.AbstractUser"""

    #TODO: Make the username case-insensitive
    slug = models.SlugField(blank=False, null=False) # Will be defaulted to slugified of username in signals.py

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})


class Profile(models.Model):
    """A model that adds bio and profile_picture to the User model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=get_upload_path, blank=True, storage=OverwriteStorage)
    slug = models.SlugField(blank=False, null=False) # Will be defaulted to slugified of username in signals.py

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})
