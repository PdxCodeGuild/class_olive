from rest_framework import serializers
from movies.models import Movie
from users.models import CustomUser
from movies.models import Movie

class NestedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movie_user' 'title', 'rating', 'have_watched')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')

class MovieSerializer(serializers.ModelSerializer):
    user_detail = NestedUserSerializer(many=True, source='users', read_only=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'rating', 'movie_user', 'have_watched', 'user_detail')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')
