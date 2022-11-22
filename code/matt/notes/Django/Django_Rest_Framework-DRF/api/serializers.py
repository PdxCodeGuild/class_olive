from rest_framework import serializers
from users.models import CustomUser

from books.models import Book

class NestedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'genre', 'author', 'isbn')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')

class BookSerializer(serializers.ModelSerializer):
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Book
        fields = ('id', 'title', 'genre', 'author', 'isbn', 'author_detail')

class UserSerializer(serializers.ModelSerializer):
    book_detail = NestedBookSerializer(many=True, source='books', read_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'books', 'book_detail')