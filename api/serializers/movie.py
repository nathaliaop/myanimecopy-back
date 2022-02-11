from rest_framework import serializers
from api.models.movie import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'genres', 'studio', 'director', 'title', 'description', 'release_date', 'image']
        depth = 2