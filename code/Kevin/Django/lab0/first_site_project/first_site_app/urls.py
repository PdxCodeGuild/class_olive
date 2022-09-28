from django.urls import path
from . import views

app_name = 'first_site_app'
urlpatterns = [
    path('', views.site_view, name='site_view'),
    path('site_create/', views.site_create, name='site_create')
]