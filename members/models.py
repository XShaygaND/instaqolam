from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

from .storage import OverwriteStorage


def get_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'{instance.user.username}/profile_picture.{extension}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=get_upload_path, blank=True, storage=OverwriteStorage)
    slug = models.SlugField(blank=False, null=False)

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})

        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)
