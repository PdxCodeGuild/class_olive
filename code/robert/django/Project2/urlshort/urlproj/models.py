import code
from nturl2path import url2pathname
import re
from django.db import models
from django.forms import CharField
from requests import request

class ShortenedURL(models.Model):
    code = models.CharField(max_length=10)
    url = models.URLField(max_length=100)

    def __str__(self):
        return self.code
