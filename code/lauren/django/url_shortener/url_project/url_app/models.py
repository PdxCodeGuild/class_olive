from django.db import models

class ShortenedURL(models.Model):
    code = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.code