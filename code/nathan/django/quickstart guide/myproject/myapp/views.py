from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from .models import Person

def myview(request):
    person = Person.objects.all()

    context = {
        'person': person
    }

    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    name = request.POST['name']
    height = request.POST['height']
    weight = request.POST['weight']

    Person.objects.create(name=name, height=height, weight=weight)
    return HttpResponseRedirect(reverse('myapp:myview'))