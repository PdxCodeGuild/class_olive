from unittest.util import _MAX_LENGTH
from django.db import models

class URLs(models.Model):
    long_url = models.TextField(max_length=200)
    short_url = models.TextField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description