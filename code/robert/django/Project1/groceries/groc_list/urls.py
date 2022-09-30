from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'groc_list'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_groc', views.add_groc, name='add_groc')
]