from django.db import models
import datetime

class GroceryItem(models.Model):
    item_name = models.CharField(max_length=200)
    created_date = models.DateField(default=datetime.datetime.now())
    in_cart = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_name