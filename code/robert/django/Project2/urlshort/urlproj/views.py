from django.shortcuts import render
from django.http import HttpResponse
import string
import random

from .models import ShortenedURL

def home(request):
    all_shorts = ShortenedURL.objects.all()
    context= {
        'ShortenedURL': all_shorts
    }
    return render(request, 'urlproj'/home.html, context)

def url_short():
    code =''
    for items in range(0,9):
        code +=random.choice(string.ascii_lowercase)
    return code