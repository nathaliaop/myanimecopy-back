from rest_framework import serializers
from api.models.seasonstatus import SeasonStatus

class SeasonStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonStatus
        fields = ['id', 'progress', 'season']
        depth = 3