from django.urls import path
from . import views

app_name = 'grocery_list_app'
urlpatterns = [
    path('', views.site_view, name='site_view'),
    path('item_create/', views.item_create, name='item_create'),
    path('item_toggle/<int:id>/', views.item_toggle, name='item_toggle'),
    path('item_delete/<int:id>/', views.item_delete, name='item_delete' ),
    path('make_favorite/<int:id>/', views.make_favorite, name='make_favorite'),
    path('make_from_favorites/<int:id>/', views.make_from_favorites, name='make_from_favorites')
]