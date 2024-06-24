from django.db import models

from users.models import CustomUser



class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey(CustomUser, related_name="movie", on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
