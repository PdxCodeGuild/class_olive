from rest_framework import serializers
from users.models import CustomUser

from todo.models import ToDo, Favorites

class NestedToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'item', 'author', 'needs_doing')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')

class NestedFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'favorite', 'author')

class FavoritesSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Favorites
        fields = ('id', 'favorite', 'author', 'author_detail')

class ToDoSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = ToDo
        fields = ('id', 'item', 'author', 'needs_doing', 'author_detail')

class UserSerializer(serializers.ModelSerializer):
    todo_detail = NestedToDoSerializer(many=True, source='todo', read_only=True)
    favorites_detail = NestedFavoritesSerializer(many=True, source='favorites', read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'todo', 'todo_detail','favorites', 'favorites_detail')