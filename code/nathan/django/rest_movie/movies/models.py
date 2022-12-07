from django.db import models
from users.models import CustomUser

class Movie(models.Model):
    title = models.CharField(max_length=200)
    have_watched = models.BooleanField(default=False)
    rating = models.IntegerField(null=True)
    movie_user = models.ForeignKey(CustomUser,related_name="movies",on_delete=models.CASCADE)

    def __str__(self):
        return self.title