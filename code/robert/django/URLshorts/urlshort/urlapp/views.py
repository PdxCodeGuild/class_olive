import code
from math import comb
from textwrap import shorten
from webbrowser import get
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import string
import random

from numpy import short
from .models import ShortenedURL

code_list = []

def home(request):
    
    if request.method  == 'POST':
        url_to_code = request.POST.get('url')
        name=request.POST.get('name')
        url_code = ''.join(random.choices((string.ascii_letters+string.digits),k=5))
        if ShortenedURL.objects.filter(url=url_to_code):
            print('Already Exists')
        else:
            ShortenedURL.objects.create(url=url_to_code,code=url_code,name=name)
    
    context = {
        'shortened': ShortenedURL.objects.all()
    }
   
    return render(request, 'urlapp/home.html',context)

def redirect_view(request, url_code):
    get_code = ShortenedURL.objects.get(code=url_code).url
    return HttpResponseRedirect(get_code)