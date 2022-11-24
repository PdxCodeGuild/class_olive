from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    favorite_movie = models.CharField(max_length=200, null=True)
    favorite_genre = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username