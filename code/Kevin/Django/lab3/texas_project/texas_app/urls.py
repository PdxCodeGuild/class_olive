from django.urls import path
from . import views

app_name = 'texas_app'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete'),
    path('post/<int:pk>/edit/', views.EditPost.as_view(), name='edit' )
]