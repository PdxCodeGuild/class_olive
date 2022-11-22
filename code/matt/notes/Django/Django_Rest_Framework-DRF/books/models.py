from django.db import models

from users.models import CustomUser

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, related_name="books", on_delete=models.CASCADE)
    isbn = models.CharField(max_length=200)

    def __str__(self):
        return self.title