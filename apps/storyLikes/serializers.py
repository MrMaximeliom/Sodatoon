from apps.episodes.models import  Episode
from rest_framework import serializers
from apps.stories.serializers import StorySerializer
from apps.accounts.serializers import UserSerializer
class StoryLikesSerializer(serializers.ModelSerializer):
    story = StorySerializer(many=False, read_only=True)
    story_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Episode
        fields = '__all__'