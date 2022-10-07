from django.db import models

class URLModel(models.Model):
    url_name = models.CharField(max_length=200, null=True)
    long_url_field = models.URLField(max_length=200, null=True)
    short_url_code = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return str(self.url_name)

        