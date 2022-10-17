from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new'),
    path('post/<int:pk>/edit/', views.EditPostView.as_view(), name='edit' ),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete'),
]  