from apps.contests.serializers import ContestParticipantsSerializer,ContestSerializer
from apps.contests.models import ContestParticipants,Contest
from sodatoon.permissions import IsArtist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets


class ContestParticipantsViewSet(viewsets.ModelViewSet):
    queryset = ContestParticipants.objects.all().order_by('id')
    serializer_class = ContestParticipantsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]


class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all().order_by('id')
    serializer_class = ContestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]