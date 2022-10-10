from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from .models import URLs
import random

def shorten(url):
    url = url.strip('http')
    url = url.strip('s')
    url = url.strip('://')
    url = url.strip('www.')
    for x in range(len(url)):
        if url[x] == '/':
            url = url[:x + 1]
            break
    for x in range(5):
        url += str(random.randint(0, 9))
    return url
    

def index(request):
    urls = URLs.objects.all()
    context = {
        'urls': urls
    }
    return render(request, 'url_shortener_app/index.html', context)

def shorten_url(request):
    description = request.POST['description']
    long_url = request.POST['long_url']
    short_url = shorten(long_url)
    urls = URLs(description=description, long_url=long_url, short_url=short_url)
    urls.save()
    return redirect('url_shortener_app:index')

def redirect_url(request, id):
    url = get_object_or_404(URLs, id=id)
    return HttpResponseRedirect(url.long_url)