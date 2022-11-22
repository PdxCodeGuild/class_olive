from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):

    cover = serializers.ImageField(required=False)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'metacritic', 'cover')