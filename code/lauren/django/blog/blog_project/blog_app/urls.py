from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('post/new/', views.PostCreateView.as_view(), name='new'),
    path('post/<int:pk>/', views.Test.as_view(), name='detail')
]