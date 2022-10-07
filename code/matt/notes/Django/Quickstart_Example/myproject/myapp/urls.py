from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('new_post_url', views.new_post, name='new_post_url_name'),
    path('edit/<int:id>/', views.edit_post, name='edit_post')
]
