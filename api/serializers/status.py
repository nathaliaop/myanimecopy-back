from rest_framework import serializers
from api.models.status import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'favorite', 'progress', 'movie', 'anime', 'manga']
        depth = 3 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value