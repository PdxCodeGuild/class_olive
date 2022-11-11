from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    code = models.CharField(max_length=10)
    url = models.URLField(max_length=100, unique = True)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.code
