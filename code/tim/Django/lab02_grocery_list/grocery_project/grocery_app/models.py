from django.db import models
import datetime

class GroceryModel(models.Model):
    grocery_name = models.CharField(max_length=200, null=True)
    grocery_comment = models.CharField(max_length=200, default='', null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.grocery_name