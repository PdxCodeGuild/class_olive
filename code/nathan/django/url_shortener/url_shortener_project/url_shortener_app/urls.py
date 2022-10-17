from django.urls import path
from . import views

app_name = 'url_shortener_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten_url', views.shorten_url, name="shorten_url"),
    path('redirect_url/<int:id>', views.redirect_url, name="redirect_url")
]