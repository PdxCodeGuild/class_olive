from rest_framework import serializers
from movieapp.models import Movie
from users.models import CustomUser

class NestedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'director', 'release_date', 'author', 'opinion', 'likes', 'poster')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')


class MovieSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'director', 'release_date', 'opinion', 'author_detail', 'author', 'likes', 'poster')
        
class UserSerializer(serializers.ModelSerializer):
    movie_detail = NestedMovieSerializer(many=True, source='movies', read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'movies', 'movie_detail')
        

        
        

        
        
