from rest_framework import serializers
from api.models.episodestatus import EpisodeStatus

class EpisodeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeStatus
        fields = ['id', 'progress', 'episode']
        depth = 3