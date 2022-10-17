from django.urls import path
from . import views

app_name = 'url_shorter_app'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('url_shortener/', views.url_shortener, name='url_shortener'),
    path('url_link/<int:id>/', views.url_link, name="url_link")
]