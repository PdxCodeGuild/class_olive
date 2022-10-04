from xmlrpc.client import boolean
from django.db import models
from datetime import datetime

class GroceryItem(models.Model):
    description = models.TextField(max_length=200)
    created_date = models.DateField(default=datetime.now().date())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Settings(models.Model):
    dark_mode = models.BooleanField(default=False)
