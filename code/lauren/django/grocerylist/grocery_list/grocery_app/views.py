from django.shortcuts import render, reverse, redirect,  get_object_or_404
from django.http import HttpResponseRedirect
from .models import Groceries

def home_view(request):
    grocery_items = Groceries.objects.all()
    context = {
        'grocery_items': grocery_items
    }
    return render(request, 'grocery_app/mytemplate.html', context)


def new_item(request):
    # print('!!!!!!!!!!!!!!!!!!!!!!!!', request.POST)

    item = request.POST['item']
    expiration_date = request.POST['expiration_date']
    description = request.POST['description']
    in_cart = request.POST['in_cart']

    if in_cart == 'on':
        in_cart = True
    else:
        in_cart = False
    grocery_model=Groceries(item=item, expiration_date=expiration_date, description=description, in_cart=in_cart)
    grocery_model.save()
    return redirect('grocery_app:home')

def toggle_in_cart(request, id):
    # print("Movie ID", id)
    grocery_obj = get_object_or_404(Groceries, id=id)
    # print(movie_obj.in_theatres)

    grocery_obj.in_cart = not grocery_obj.in_cart
    grocery_obj.save()

    return redirect('grocery_app:home')

def delete_item(request, id):
    grocery_obj = get_object_or_404(Groceries, id=id)
    grocery_obj.delete()
    
    return redirect('grocery_app:home')