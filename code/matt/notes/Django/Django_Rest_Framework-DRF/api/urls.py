from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('books', views.PostBookSet, basename='book')

urlpatterns = router.urls + [
]
    # path('', views.BookAPIView.as_view()),

