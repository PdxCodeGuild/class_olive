from django.db import models
import datetime

# Create your models here.
class MyModel(models.Model):
    post_title = models.CharField(max_length=200, null=True)
    post_date = models.DateTimeField(blank=True, null=True,default=datetime.datetime.now)
    post_body = models.TextField(max_length=600, null=True)
    
    def __str__(self):
        return self.post_title 
        return self.post_date
        return self.post_body