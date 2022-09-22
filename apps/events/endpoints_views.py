from apps.events.serializers import EventSerializer,EventParticipantsSerializer
from apps.events.models import Event,EventParticipants
from sodatoon.permissions import IsArtist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]


class EventParticipantsViewSet(viewsets.ModelViewSet):
    queryset = EventParticipants.objects.all().order_by('id')
    serializer_class = EventParticipantsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]