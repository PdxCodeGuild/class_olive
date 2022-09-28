from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class InputClass(models.Model):
    input_field = models.CharField(max_length=200)
    body = models.TextField(max_length=200, null=True)
    author = models.CharField(max_length=20, null=True)
    date_time = models.TimeField(default=datetime.now, null=True)
    
    def __str__(self):
        return self.input_field