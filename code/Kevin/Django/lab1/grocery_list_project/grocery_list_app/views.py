from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import HttpResponseRedirect
from .models import GroceryItem

def site_view(request):
    grocery_items = GroceryItem.objects.all()
    context = {
        'grocery_items': grocery_items
    }
    return render(request, 'grocery_list_app/home.html', context)

def item_create(request):
    item_name = request.POST['item_name']
    grocery_item = GroceryItem(item_name=item_name)
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list_app:site_view'))

def item_toggle(request, id):
        item = get_object_or_404(GroceryItem, id=id)
        if item.in_cart == True:
            item.in_cart = False
        else:
            item.in_cart = True

        item.save()

        return redirect('grocery_list_app:site_view')

def item_delete(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.delete()

    return redirect('grocery_list_app:site_view')
    

        

        
        