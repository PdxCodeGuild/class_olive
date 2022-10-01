from django.urls import path
from . import views

app_name = 'grocery_list_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('creategroceryitem/', views.create_grocery_item, name='create_grocery_item'),
    path('completethisitme/<int:id>/', views.complete_this_item, name='complete_this_item' ),
    path('settings/', views.to_settings, name='to_settings'),
    path('resetthisitem/<int:id>/', views.reset_this_item, name='reset_this_item' ),
    path('changemode/', views.change_mode, name='change_mode'),
    path('deleteitem/<int:id>/', views.delete_item, name='delete_item')
]
