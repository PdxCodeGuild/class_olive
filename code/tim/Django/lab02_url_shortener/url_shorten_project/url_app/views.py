from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import URLModel
import string, random

def home(request):
    url_instances = URLModel.objects.all()
    context = {
        'url_instances': url_instances
    }
    return render(request, 'url_app/home.html', context)

def random_code():
    short_url_code = ''
    for x in range(7):
        short_url_code += ''.join(random.choice(string.ascii_letters + string.digits)) 
    return short_url_code


def shorturl(request):
    if request.method == 'POST':
        url_name = request.POST['url_name']
        long_url_field = request.POST['long_url_field']
        short_url_code = random_code()
        URLModel.objects.create(url_name=url_name, long_url_field=long_url_field, short_url_code=short_url_code)
        return redirect( 'url_app:home') 
    else:
        url_instances = URLModel.objects.all()
        context = {
            'url_instances': url_instances
        }
        return render(request, 'url_app/home.html', context )

def redirect_to_long(request, short_url_code):
    url_obj = get_object_or_404(URLModel, short_url_code=short_url_code)
    url = url_obj.long_url_field
    return HttpResponseRedirect(url)