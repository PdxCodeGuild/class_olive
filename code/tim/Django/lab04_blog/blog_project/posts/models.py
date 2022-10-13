from django.db import models
from django.urls import reverse

class Blog_Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", args=(self.pk,))