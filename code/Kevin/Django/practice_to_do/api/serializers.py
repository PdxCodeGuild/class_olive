from rest_framework import serializers
from users.models import CustomUser

from todo.models import ToDo

class NestedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'item', 'author', 'needs_doing')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')

class ToDoSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = ToDo
        fields = ('id', 'item', 'author', 'needs_doing', 'author_detail')

class UserSerializer(serializers.ModelSerializer):
    book_detail = NestedBookSerializer(many=True, source='todo', read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'todo', 'book_detail')