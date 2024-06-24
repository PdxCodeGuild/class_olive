from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username
