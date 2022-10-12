from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile')
]

    
    
    
    # path('', views.home_view, name='home'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
