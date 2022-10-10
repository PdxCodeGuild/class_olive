from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import GroceryModel

def home_view(request):
    groceries = GroceryModel.objects.all()
    context = {
        'groceries': groceries
    }
    return render(request, 'grocery_app/home.html', context)

def add_to_list(request):
    grocery_name = request.POST['grocery_name']
    grocery_comment = request.POST['grocery_comment']
    grocery = GroceryModel(grocery_name=grocery_name, grocery_comment=grocery_comment)
    print("!!!!!!!!!!!!!!!!!!", grocery.grocery_name, "was added to Shopping list") 
    grocery.save()
    return redirect('grocery_app:home_view')

def toggle_completed(request, id):
    grocery_obj = get_object_or_404(GroceryModel, id=id)
    print("!!!!!!!!!!!!!!!!!!", grocery_obj.grocery_name, ", ID", id, "was moved to other list")
    grocery_obj.completed = not grocery_obj.completed
    grocery_obj.save()
    return redirect('grocery_app:home_view')

def delete_grocery(request, id):
    grocery_obj = get_object_or_404(GroceryModel, id=id)
    print("!!!!!!!!!!!!!!!!!!", grocery_obj.grocery_name, ", ID", id, "was deleted from lists.")
    grocery_obj.delete()
    return redirect('grocery_app:home_view')

