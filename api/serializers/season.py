from rest_framework import serializers
from api.models.season import Season
from api.serializers.episode import EpisodeSerializer

class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)
    class Meta:
        model = Season
        fields = ['id', 'number', 'episodes']
        depth = 1