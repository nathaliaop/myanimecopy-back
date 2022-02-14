from rest_framework import serializers
from api.models.episode import Episode

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'name', 'number']
        depth = 2
