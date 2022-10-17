from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    height = models.CharField(max_length=4)
    weight = models.CharField(max_length=4)
    
    def __str__(self):
        return self.name
