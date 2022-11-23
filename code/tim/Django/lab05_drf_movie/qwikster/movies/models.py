from django.db import models

from users.models import CustomUser

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    metacritic = models.CharField(max_length=200)
    addedBy = models.ForeignKey(CustomUser, related_name="movies", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
    # cover = models.ImageField(upload_to ='uploads/', blank=True, null=True)