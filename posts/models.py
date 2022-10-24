from typing import OrderedDict
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from datetime import datetime
import uuid

from members.storage import OverwriteStorage

from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

User = settings.AUTH_USER_MODEL


def get_upload_path(instance, filename):
    """Returns {instance.unique_id}/logo.{file_extension}"""

    extension = filename.split('.')[-1]
    return f'{instance.unique_id}/logo.{extension}'


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    """A class for models that use UUID as pk for django.taggit"""

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
    

class Post(models.Model):
    """A basic post model that uses UUID(unique_id) as its pk and has the fields: unique_id, title, body, author, logo, pub_date, likes and tags
    A placeholder is not created when logo field is empty, Therefore it's recommended to create a static placeholder file"""

    unique_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=75)
    body = models.TextField()
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=get_upload_path, blank=True, storage=OverwriteStorage)
    pub_date = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    tags = TaggableManager(through=UUIDTaggedItem, blank=True)

    def number_of_likes(self):
        return self.likes.count()


    def __str__(self):
        return str(self.author) + ' | ' + self.title

    def get_absolute_url(self):
        return reverse('details', args=((self.pk,)))

    
class Comment(models.Model):
    """A basic comment model that has the fields: post, user, body and pub_date
    you can change the user's model to EmailField or CharField if you want non-authorizes users to be able to comment"""
    
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return f"{str(self.user)} | on: {self.post.title[:20]}(by {self.post.author}) | {self.body[:20]}"
