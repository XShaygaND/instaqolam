from email.policy import default
from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=75)
    body = models.TextField()
    logo = models.ImageField(upload_to=f'user_data/', default='static/placeholder.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.author) + ' | ' + self.title
