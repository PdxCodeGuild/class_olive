from rest_framework import serializers
from movies.models import Movie
from users.models import CustomUser

class NestedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'metacritic', 'addedBy', 'onNetflix', 'onHulu', 'onAmazon', 'onHBO')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')

class MovieSerializer(serializers.ModelSerializer):
    addedBy_detail = NestedUserSerializer(read_only=True, source='addedBy')
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'metacritic', 'addedBy', 'addedBy_detail', 'onNetflix', 'onHulu', 'onAmazon', 'onHBO')

class UserSerializer(serializers.ModelSerializer):
    movie_detail = NestedMovieSerializer(many=True, source='movies', read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'movies', 'movie_detail')