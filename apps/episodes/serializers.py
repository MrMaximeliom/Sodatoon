from apps.episodes.models import  Episode
from rest_framework import serializers
from apps.stories.serializers import StorySerializer
class EpisodeSerializer(serializers.ModelSerializer):
    story = StorySerializer(many=False, read_only=True)
    story_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Episode
        fields = '__all__'