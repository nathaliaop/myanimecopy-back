from rest_framework import serializers
from api.models.seasonstatus import SeasonStatus
from api.serializers.episodestatus import EpisodeStatusSerializer

class SeasonStatusSerializer(serializers.ModelSerializer):
    episodestatus = EpisodeStatusSerializer(many=True)
    class Meta:
        model = SeasonStatus
        fields = ['id', 'progress', 'season', 'episodestatus']
        depth = 3