from rest_framework import serializers
from api.models.social import Social

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'followers', 'following']
        depth = 3