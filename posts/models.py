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
    extension = filename.split('.')[-1]
    return f'{instance.unique_id}/logo.{extension}'


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
    

class Post(models.Model):

    unique_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=75)
    body = models.TextField()
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=get_upload_path, blank=True, storage=OverwriteStorage)
    pub_date = models.DateTimeField(default=datetime.now())
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    tags = TaggableManager(through=UUIDTaggedItem)

    def number_of_likes(self):
        return self.likes.count()


    def __str__(self):
        return str(self.author) + ' | ' + self.title

    def get_absolute_url(self):
        return reverse('details', args=((self.pk,)))
