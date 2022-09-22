from apps.episodes.models import  Episode
from rest_framework import serializers
from apps.episodes.serializers import EpisodeSerializer
from apps.accounts.serializers import UserSerializer
class EpisodeLikesSerializer(serializers.ModelSerializer):
    episode = EpisodeSerializer(many=False, read_only=True)
    episode_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Episode
        fields = '__all__'