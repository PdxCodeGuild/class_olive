from django.urls import path
from . import views

app_name = 'grocery_app'
urlpatterns = [
        path('', views.home_view, name='home'),
    path('add_new_item', views.new_item, name='add_new_item'),
    path('toggle/<int:id>/', views.toggle_in_cart, name='toggle_in_cart'),
    
]