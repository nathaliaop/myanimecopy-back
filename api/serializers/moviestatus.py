from rest_framework import serializers
from api.models.moviestatus import MovieStatus

class MovieStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieStatus
        fields = ['id', 'favorite', 'progress', 'movie']
        depth = 3