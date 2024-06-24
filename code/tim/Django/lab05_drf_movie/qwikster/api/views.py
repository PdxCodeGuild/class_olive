from movies.models import Movie
from .serializers import MovieSerializer
from rest_framework import generics, viewsets, permissions
# from rest_framework.parsers import MultiPartParser, FormParser

class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class PostMovieSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer