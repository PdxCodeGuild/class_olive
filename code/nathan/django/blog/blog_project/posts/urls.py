from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create_post/', views.Create_post.as_view(), name='create_post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete')
]