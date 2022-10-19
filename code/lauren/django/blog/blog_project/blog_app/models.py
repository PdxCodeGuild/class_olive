from django.db import models

from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', related_name='blog_app', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=250)
    public = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_app:detail", args=(self.pk,))
