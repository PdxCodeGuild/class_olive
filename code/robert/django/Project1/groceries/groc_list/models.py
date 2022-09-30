from django.db import models

# Create your models here.
class Groceries(models.Model):
    item = models.CharField(max_length=50)
    created_date = models.DateTimeField(null=True)
    comp = models.BooleanField(default=False)

    def __str__(self):
        return self.item 