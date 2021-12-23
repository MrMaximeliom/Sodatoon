from .serializers import \
    CommentsSerializer, EventSerializer, \
    StorySerializer, EpisodeSerializer, \
    EventParticipantsSerializer, \
    ContestSerializer, ContestParticipantsSerializer
from reader.models import Story, \
    EventParticipants, Episode, Event, \
    ContestParticipants, Contest, Comments
from sodatoon.permissions import IsArtist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('id')
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().order_by('id')
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]


class EventParticipantsViewSet(viewsets.ModelViewSet):
    queryset = EventParticipants.objects.all().order_by('id')
    serializer_class = EventParticipantsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]


class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all().order_by('id')
    serializer_class = ContestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]


class ContestParticipantsViewSet(viewsets.ModelViewSet):
    queryset = ContestParticipants.objects.all().order_by('id')
    serializer_class = ContestParticipantsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]
