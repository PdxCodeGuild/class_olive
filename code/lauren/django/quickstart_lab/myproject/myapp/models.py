from django.db import models
from datetime import datetime
class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    body = models.TextField(max_length=200, null=True)
    author = models.TextField(max_length=200, null=True)
    time = models.DateTimeField(default=datetime.now, null=True)
    
    
    
    def __str__(self):
        return self.myfield
