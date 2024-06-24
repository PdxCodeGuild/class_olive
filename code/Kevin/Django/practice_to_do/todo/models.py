from django.db import models

from users.models import CustomUser

class ToDo(models.Model):
    item = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, related_name="todo", on_delete=models.CASCADE)
    needs_doing = models.BooleanField(default=True)

    def __str__(self):
        return self.item

class Favorites(models.Model):
    favorite = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, related_name="favorites", on_delete=models.CASCADE)

    def __str__(self):
        return self.favorite