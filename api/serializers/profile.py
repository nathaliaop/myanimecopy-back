from rest_framework import serializers
from api.models.profile import Profile
from api.serializers.status import StatusSerializer

class ProfileSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'status', 'social']
        depth = 3 # returns the fields of foreign key related objects up to depth 1, instead of just a foreign key value