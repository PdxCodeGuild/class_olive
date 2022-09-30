from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Groceries

def home(request):
    groc_list = Groceries.objects.all()

    context = {
        'groc_list' : groc_list
    }
    return render(request, 'groc_list/home.html', context)

def add_groc(request):
    item = request.POST['item']
    created_date = request.POST['created_date']
    comp = request.POST['comp']

    if comp == 'on':
        comp = True
    else:
        comp = False

    groc_model = Groceries(item=item, created_date=created_date, comp=comp)
    groc_model.save()
    return redirect('groc_list:home')