from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.dispatch import receiver

from .models import Profile

User = get_user_model()

@receiver(pre_save, sender=User)
def update_user(sender, instance, **kwargs):
    """Sets user's slug to slugified user's username before saving the user"""
    instance.slug = slugify(instance.username)


@receiver(post_save, sender=User)
def create_update_profile(sender, instance, created, **kwargs):
    """Creates a profile for user and set's it's slug to slugified user's username only on user creation"""

    if created:
        Profile.objects.create(user=instance, slug=instance.slug)
    
    elif instance.profile.slug != instance.slug:
        instance.profile.slug = instance.slug
        instance.profile.save()
