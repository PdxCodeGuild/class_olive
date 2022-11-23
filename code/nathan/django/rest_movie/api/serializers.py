from rest_framework import serializers
from movies.models import Movie
from users.models import CustomUser
from movies.models import Movie

class NestedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'director', 'genre', 'release_date', 'rating')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'director', 'genre', 'release_date', 'rating')

class UserSerializer(serializers.ModelSerializer):
    movie_detail = NestedMovieSerializer(many=True, source='moives', read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'signup_date', 'favorite_movie', 'movie_detail')
