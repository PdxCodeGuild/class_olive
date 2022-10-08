from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete'),
    path('post/<int:pk>/edit/', views.EditPost.as_view(), name='edit' )
]


    # non class based example
    # path('', views.home_view, name='home')