from apps.contests.models import Contest,ContestParticipants
from rest_framework import serializers

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = "__all__"


class ContestParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestParticipants
        fields = "__all__"