from apps.stories.models import Story
from rest_framework import serializers
from apps.accounts.serializers import UserSerializer
class StorySerializer(serializers.ModelSerializer):
    episodes_count = serializers.IntegerField(min_value=1)
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Story
        fields = "__all__"

