from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'groc_list'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_groc', views.add_groc, name='add_groc'),
    path('edit/<int:id>/', views.change_comp, name='change_comp'),
    path('delete/<int:id>/', views.delete_groc, name='delete_groc')
]