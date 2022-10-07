from django.urls import path
from . import views

app_name = 'biz_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('addbiz/', views.add_your_biz, name='addbiz'),
    path('<id>', views.redirect_to_images, name='send_to_page')

]