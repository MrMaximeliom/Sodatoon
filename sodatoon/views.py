from django.shortcuts import render

from rest_framework import viewsets, mixins
from .serializers import UserSerializer, GroupSerializer,\
    CommentsSerializer,EventSerializer,\
    StorySerializer,EpisodeSerializer,\
    EventParticipantsSerializer,\
    ContestSerializer,ContestParticipantsSerializer
from reader.models import User,Story,\
    EventParticipants,Episode,Event,\
    ContestParticipants,Contest,Comments
from django.contrib.auth.models import Group
from .permissions import IsArtistT,IsArtist
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterSerializer

class CurrentUserViewSet(viewsets.ModelViewSet):
    """
      API endpoint that allows to view current user data
      """
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)










class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]
    # self.request.user




class ArtistUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.filter(is_artist=True)

class ReaderUserViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows users to be viewed or edited.
        """
        queryset = User.objects.all().order_by('-date_joined')
        serializer_class = UserSerializer
        permission_classes = [AllowAny]
        def get_queryset(self):
            return User.objects.filter(is_artist=False)


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    # def get_queryset(self):
    #     return User.objects.filter(is_artist=False)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('id')
    serializer_class = StorySerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticatedOrReadOnly,IsArtist]

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().order_by('id')
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsArtist]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsArtist]

class EventParticipantsViewSet(viewsets.ModelViewSet):
    queryset = EventParticipants.objects.all().order_by('id')
    serializer_class = EventParticipantsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsArtist]

class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all().order_by('id')
    serializer_class = ContestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsArtist]

class ContestParticipantsViewSet(viewsets.ModelViewSet):
    queryset = ContestParticipants.objects.all().order_by('id')
    serializer_class = ContestParticipantsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsArtist]

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsArtist]