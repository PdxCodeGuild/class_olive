from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path('', views.Register.as_view(), name='signup'),
    path('<str:username>/', views.UserProfile.as_view(), name='profile')
]