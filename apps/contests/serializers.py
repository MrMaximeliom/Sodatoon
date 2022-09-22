from apps.contests.models import Contest,ContestParticipants
from rest_framework import serializers
from apps.accounts.serializers import UserSerializer
class ContestSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Contest
        fields = "__all__"


class ContestParticipantsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    contest = ContestSerializer(many=True, read_only=True)
    contest_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = ContestParticipants
        fields = "__all__"