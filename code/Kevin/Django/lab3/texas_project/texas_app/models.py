from datetime import datetime
from django.db import models
from django.urls import reverse
import datetime

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", args=(self.pk,))