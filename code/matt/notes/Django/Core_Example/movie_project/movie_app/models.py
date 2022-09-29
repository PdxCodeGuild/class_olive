from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=208)
    director = models.CharField(max_length=200, default='Olive')
    release_date = models.DateTimeField(null=True)
    in_theatres = models.BooleanField(default=True)
    genre = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.title 

