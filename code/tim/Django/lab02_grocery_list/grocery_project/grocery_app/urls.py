from django.urls import path
from . import views

app_name = 'grocery_app'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('add_to_list/', views.add_to_list, name='add_to_list'),
    path('edit/<int:id>/', views.toggle_completed, name='toggle_completed'),
    path('delete/<int:id>/', views.delete_grocery, name='delete_grocery'),
]