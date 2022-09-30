from django.urls import path
from . import views

app_name = 'grocery_list_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('creategroceryitem/', views.create_grocery_item, name='create_grocery_item')
]
