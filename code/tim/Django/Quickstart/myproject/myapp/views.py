from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import MyModel

def myview(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'myapp/mytemplate.html', context)

def mycreate(request):
    post_title = request.POST['post_title']
    post_body = request.POST['post_body']
    mymodel = MyModel(post_title=post_title, post_body=post_body)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))

# def index(request):
#     return HttpResponse('you are at the index')

def about(request):
    return HttpResponse('you are at the About page')