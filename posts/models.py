from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime

def get_file_path(instance, filename):
    file_extension = filename.split('.')[-1]
    return f'user_{instance.author}/{instance.pub_date.strftime("%Y/%B/%a-%M")}/logo.{file_extension}'


class Post(models.Model):

    title = models.CharField(max_length=75)
    body = models.TextField()
    logo = models.ImageField(upload_to=get_file_path, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return str(self.author) + ' | ' + self.title

    def get_absolute_url(self):
        return reverse('details', args=((self.pk,)))
