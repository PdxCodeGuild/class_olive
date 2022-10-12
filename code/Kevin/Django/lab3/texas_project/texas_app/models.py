from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title