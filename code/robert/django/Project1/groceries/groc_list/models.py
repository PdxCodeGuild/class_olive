from django.db import models

# Create your models here.
class Groceries(models.Model):
    brand = models.CharField(max_length=50, default='Generic')
    item = models.CharField(max_length=50)
    created_date = models.DateField(null=True)
    comp = models.BooleanField(default=False)
    store = models.CharField(max_length=50,default='S&S')
    coupon = models.BooleanField(default=False)

    def __str__(self):
        return self.item