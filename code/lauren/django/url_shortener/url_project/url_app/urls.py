from django.urls import path
from . import views

app_name = 'url_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('shortener/', views.shorten_url, name='shortener'),
    path('<id>', views.redirect_to_url, name='send_to_page')
]