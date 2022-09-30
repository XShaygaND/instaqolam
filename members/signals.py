from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.dispatch import receiver

from .models import Profile

User = get_user_model()

@receiver(pre_save, sender=User)
def create_user(sender, instance, **kwargs):
    instance.slug = slugify(instance.username)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, slug=instance.slug)
