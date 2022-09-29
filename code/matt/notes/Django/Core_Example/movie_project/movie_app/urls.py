from django.urls import path
from . import views

app_name = 'movie_app'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('add_new_movie', views.new_movie, name='add_new_movie'),
    path('edit/<int:id>/', views.toggle_in_theatres, name='toggle_in_theatres'),
    path('delete/<int:id>/', views.delete_movie, name='delete_route')
]