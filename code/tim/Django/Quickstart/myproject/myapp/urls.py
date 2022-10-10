from django.urls import path
from . import views

# app_name = 'myapp'
# urlpatterns = [
#     path('myview/', views.myview, name='myview'),
#     path('mycreate/', views.mycreate, name='mycreate'),

    # path('', views.index, name='index'),
    # path('mycreate/', views.mycreate, name='mycreate'),
    # localhost:8000/mypath/about/
    # path('about/', views.about, name='about'),
# ]

app_name = 'myapp'
urlpatterns = [
    # localhost:8000/mypath/
    # path('', views.index, name='index'),
    # localhost:8000/mypath/about/
    path('about/', views.about, name='about'),
    path('', views.myview, name='myview'),
    path('mycreate/', views.mycreate, name='mycreate'),

]