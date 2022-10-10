from django.shortcuts import redirect, render, get_object_or_404
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
    comp = request.POST.get('comp', False)
    store = request.POST['store']
    brand = request.POST['brand']
    coupon = request.POST.get('coupon',False)

    groc_model = Groceries(item=item, created_date=created_date, comp=comp, store=store, brand=brand, coupon=coupon)
    groc_model.save()
    return redirect('groc_list:home')

def delete_groc(request, id):
    groc_model = get_object_or_404(Groceries, id=id)
    groc_model.delete()
    return redirect('groc_list:home')

def change_comp(request, id):
    groc_model = get_object_or_404(Groceries, id=id)
    groc_model.comp = not groc_model.comp
    groc_model.save()

    return redirect('groc_list:home')
