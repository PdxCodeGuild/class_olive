from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title 