from django.db import models

class Biz(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self):
        return  self.name