from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    metacritic = models.CharField(max_length=200)
    cover = models.ImageField(upload_to ='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title