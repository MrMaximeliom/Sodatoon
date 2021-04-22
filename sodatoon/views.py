from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer,\
    CommentsSerializer,EventSerializer,\
    StorySerializer,EpisodeSerializer,\
    EventParticipantsSerializer,\
    ContestSerializer,ContestParticipantsSerializer
from reader.models import User,Story,\
    EventParticipants,Episode,Event,\
    ContestParticipants,Contest,Comments
from django.contrib.auth.models import Group
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('id')
    serializer_class = StorySerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().order_by('id')
    serializer_class = EpisodeSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer

class EventParticipantsViewSet(viewsets.ModelViewSet):
    queryset = EventParticipants.objects.all().order_by('id')
    serializer_class = EventParticipantsSerializer

class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all().order_by('id')
    serializer_class = ContestSerializer

class ContestParticipantsViewSet(viewsets.ModelViewSet):
    queryset = ContestParticipants.objects.all().order_by('id')
    serializer_class = ContestParticipantsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsSerializer