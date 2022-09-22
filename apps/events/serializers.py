from apps.events.models import Event,EventParticipants
from rest_framework import serializers
from apps.accounts.serializers import UserSerializer

class EventSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Event
        fields = '__all__'



class EventParticipantsSerializer(serializers.ModelSerializer):
    event = EventSerializer(many=True, read_only=True)
    event_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(many=True, read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = EventParticipants
        fields = "__all__"
