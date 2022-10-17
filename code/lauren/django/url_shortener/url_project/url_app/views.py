
from nturl2path import url2pathname
from .models import ShortenedURL
import random
import string
from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.http import HttpResponseRedirect


def random_code():
    code = ''
    for x in range(6):
        code += random.choice(string.ascii_letters)
    return code

def home(request):
    all_urls = ShortenedURL.objects.all()
    context = {
        'urls': all_urls 
    }
    return render(request, 'url_app/mytemplate.html', context)

def shorten_url(request):
    if request.method == 'POST':
        all_urls = ShortenedURL.objects.all()
        url = request.POST['url']
        code = random_code()
        ShortenedURL.objects.create(url=url, code=code)
        
        return redirect( 'url_app:home') 

    else:
        all_urls = ShortenedURL.objects.all()
        context = {
            'urls': all_urls
        }
        return render(request, 'url_app/mytemplate.html', context )
    
def redirect_to_url(request, id):
    url_obj = get_object_or_404(ShortenedURL, id=id)
    print(url_obj.url)

    return HttpResponseRedirect(url_obj.url)
    