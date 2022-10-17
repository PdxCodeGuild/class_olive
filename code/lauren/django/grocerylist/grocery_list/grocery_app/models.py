from django.db import models

class Groceries(models.Model):
    item = models.CharField(max_length=200)
    expiration_date = models.DateField(max_length=200)
    in_cart = models.BooleanField(default=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.item