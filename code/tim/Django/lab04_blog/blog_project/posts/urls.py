from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new'),
]
    