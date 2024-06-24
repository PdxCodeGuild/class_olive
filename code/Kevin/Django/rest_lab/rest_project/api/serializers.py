from rest_framework import serializers

from rest_app.models import Movie
from users.models import CustomUser

class NestedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'director', 'genre',)

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')

class MovieSerializer(serializers.ModelSerializer):
    director_detail = NestedUserSerializer(read_only=True, source='director')
    class Meta:
        model = Movie
        fields = ('id', 'title', 'director', 'genre', 'director_detail')

class UserSerializer(serializers.ModelSerializer):
    movie_detail = NestedMovieSerializer(many=True, source='movie', read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'favorite_movie', 'favorite_genre', 'email', 'movie_detail')

