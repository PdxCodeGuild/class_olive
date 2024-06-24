from django.db import models
from users.models import CustomUser

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, related_name="movies", on_delete=models.CASCADE)
    release_date = models.DateField(max_length=50, null=True)
    opinion = models.TextField(null=True)
    likes = models.IntegerField(default=0)
    # public = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    poster = models.ImageField(upload_to='images/', null=True)
    
def __str__(self):
    return self.title