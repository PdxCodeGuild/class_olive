from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('<str:username>/', views.Profile.as_view(), name='profile')
]