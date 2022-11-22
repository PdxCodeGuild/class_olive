from django.urls import path
from . import views
from .views import MovieListView


app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='home')
]
