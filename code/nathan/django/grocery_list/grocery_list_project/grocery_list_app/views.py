from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import GroceryItem

context = {
    'message': "Hello World"
}

def index(request):
    grocery_list = GroceryItem.objects.all()

    return render(request, 'grocery_list_app/index.html', {'grocery_list': grocery_list})

def create_grocery_item(request):
    description = request.POST['description']
    grocery_item = GroceryItem(description=description)
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list_app:index'))
