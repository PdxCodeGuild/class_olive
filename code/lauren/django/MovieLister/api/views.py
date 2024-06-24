from rest_framework import generics, viewsets

from movieapp.models import Movie
from.serializers import MovieSerializer

class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class PostMovieSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer