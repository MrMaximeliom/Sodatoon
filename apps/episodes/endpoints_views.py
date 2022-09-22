from apps.episodes.serializers import EpisodeSerializer
from apps.episodes.models import Episode
from sodatoon.permissions import IsArtist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().order_by('id')
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]