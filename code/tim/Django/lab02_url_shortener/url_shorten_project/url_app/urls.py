from django.urls import path
from . import views

app_name = 'url_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('shorten/', views.shorturl, name='shorten_url'),
    path('<short_url_code>/', views.redirect_to_long, name='send_to_page'),
]