from apps.events.models import Event,EventParticipants
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'



class EventParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipants
        fields = "__all__"
