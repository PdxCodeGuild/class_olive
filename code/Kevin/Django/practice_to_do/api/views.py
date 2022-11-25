from rest_framework import generics, viewsets

from todo.models import ToDo
from .serializers import ToDoSerializer

class ToDoAPIView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class PostToDoSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer