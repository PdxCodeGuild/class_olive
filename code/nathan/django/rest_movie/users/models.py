from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
from datetime import date

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    signup_date = models.DateField(default=date.today)
    favorite_movie = models.ForeignKey(Movie, related_name="favorite_movie", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username
