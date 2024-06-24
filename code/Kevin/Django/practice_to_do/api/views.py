from rest_framework import generics, viewsets

from todo.models import ToDo, Favorites
from .serializers import ToDoSerializer, FavoritesSerializer

class ToDoAPIView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class PostToDoSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class FavoritesAPIView(generics.ListAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

class PostFavoritesSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer