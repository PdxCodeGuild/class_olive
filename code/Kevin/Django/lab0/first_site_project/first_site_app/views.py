from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import InputClass, InputClass

def site_view(request):
    instances = InputClass.objects.all()
    context = {
        'instances': instances
    }
    return render(request, 'first_site_app/index.html', context)

def site_create(request):
    input_field = request.POST['input_field']
    body = request.POST['body']
    author = request.POST['author']
    mymodel = InputClass(input_field=input_field, body=body, author=author)
    mymodel.save()
    return HttpResponseRedirect(reverse('first_site_app:site_view'))