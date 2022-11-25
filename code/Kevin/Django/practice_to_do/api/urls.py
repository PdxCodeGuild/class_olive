from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('todo', views.PostToDoSet, basename='todo')

urlpatterns = router.urls + [
    path('', views.ToDoAPIView.as_view()),
]