from django.db import models

class ShorterUrlModel(models.Model):
    given_url = models.URLField(max_length=200)
    shorter_url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.given_url