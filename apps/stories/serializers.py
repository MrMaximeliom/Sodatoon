from apps.stories.models import Story
from rest_framework import serializers

class StorySerializer(serializers.ModelSerializer):
    episodes_count = serializers.IntegerField(min_value=1)
    class Meta:
        model = Story
        fields = "__all__"

