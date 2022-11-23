from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title