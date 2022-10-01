from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import HttpResponseRedirect
from .models import GroceryItem, Settings




def items_completed(items):
    for item in items:
        if item.completed:
            return True
    return False

def no_items_completed(items):
    for item in items:
        if not item.completed:
            return True
    return False

def index(request):
    settings = Settings.objects.all()
    setting_string = "light"
    if len(settings) == 0:
        my_settings = Settings()
        my_settings.save()
    else: 
        if settings[0].dark_mode:
            setting_string = "dark"
    grocery_list = GroceryItem.objects.all()
    message = ''
    which_message =''
    if not items_completed(grocery_list):
        message = "Get started completing items today!"
        which_message = "no_completed"
    if not no_items_completed(grocery_list):
        message = "Good job on completing all your items!"
        which_message = "all_completed"
    return render(request, 'grocery_list_app/index.html', {'grocery_list': grocery_list, 'message': message, 'which': which_message, 'mode': setting_string})

def create_grocery_item(request):
    description = request.POST['description']
    grocery_item = GroceryItem(description=description)
    grocery_item.save()
    return redirect('grocery_list_app:index')

def complete_this_item(request, id):
    grocery_item = get_object_or_404(GroceryItem, id=id)
    grocery_item.completed = True
    grocery_item.save()
    return redirect('grocery_list_app:index')

def to_settings(request):
    settings = Settings.objects.all()
    setting_string = "light"
    if len(settings) == 0:
        my_settings = Settings()
        my_settings.save()
    else: 
        if settings[0].dark_mode:
            setting_string = "dark"
    grocery_list = GroceryItem.objects.all()
    message = ''
    which_message = ''
    if not items_completed(grocery_list):
        message = "Get started completing items today!"
        which_message = "no_completed"
    if not no_items_completed(grocery_list):
        message = "Good job on completing all your items!"
        which_message = "all_completed"
    return render(request, 'grocery_list_app/settings.html', {'grocery_list': grocery_list, 'message': message, 'which': which_message, 'mode': setting_string})

def reset_this_item(request, id):
    grocery_item = get_object_or_404(GroceryItem, id=id)
    grocery_item.completed = False
    grocery_item.save()
    return redirect('grocery_list_app:to_settings')

def delete_item(request, id):
    GroceryItem.objects.filter(id=id).delete()
    return redirect('grocery_list_app:to_settings')

def change_mode(request):
    grocery_list = GroceryItem.objects.all()
    value = request.POST['mode']
    settings = get_object_or_404(Settings, id=1)
    if value == 'dark':
        settings.dark_mode = True
    else:
        settings.dark_mode = False
    settings.save()
    message = ''
    which_message = ''
    if not items_completed(grocery_list):
        message = "Get started completing items today!"
        which_message = "no_completed"
    if not no_items_completed(grocery_list):
        message = "Good job on completing all your items!"
        which_message = "all_completed"
    return render(request, 'grocery_list_app/settings.html', {'grocery_list': grocery_list, 'message': message, 'which': which_message, 'mode': value})

