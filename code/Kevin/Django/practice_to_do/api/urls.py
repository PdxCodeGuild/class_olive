from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('todo', views.PostToDoSet, basename='todo')
router.register('favorites', views.PostFavoritesSet, basename='favorites')

urlpatterns = router.urls + [
    path('', views.ToDoAPIView.as_view()),
    path('', views.FavoritesAPIView.as_view())
]