from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('movies', views.PostMovieSet, basename='movie')

urlpatterns = router.urls + [
]