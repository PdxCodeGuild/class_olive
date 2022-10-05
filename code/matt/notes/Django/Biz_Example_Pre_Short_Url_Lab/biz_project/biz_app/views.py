from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import random 
from .models import Biz

# not for rendering, a normal function that is later used for the context of a view
def random_phone_number():
    phone = ''
    # phone = '('
    for x in range(10):
        phone += str(random.randint(0 , 9))
        # if x == 2:
        #     phone += ')'
        # elif x == 5:
        #     phone += '-'
    return phone
        



def home(request):
    all_biz = Biz.objects.all()
    context = {
        'biz': all_biz
    }

    return render(request, 'biz_app/home.html', context)

def add_your_biz(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        # phone = request.POST['phone']
        phone = random_phone_number() # just showing python is still python and we can use the function
        email = request.POST['email']
        website = request.POST['website']
        Biz.objects.create(name=name, phone=phone, email=email, website=website)
       
        return redirect( 'biz_app:home') 

    else:
        all_biz = Biz.objects.all()
        context = {
            'biz': all_biz
        }
        return render(request, 'biz_app/addbiz.html', context )

def redirect_to_images(request, name):
    # print("!!!!!!!!!!!!!!!!!!!", name)
    url = 'https://www.google.com/search?q=' + name 

    return HttpResponseRedirect(url)