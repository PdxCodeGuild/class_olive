from rest_framework import generics, viewsets

from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PostBookSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer