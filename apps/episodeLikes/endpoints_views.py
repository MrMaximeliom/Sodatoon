from apps.episodeLikes.serializers import EpisodeLikesSerializer
from apps.episodeLikes.models import EpisodeLike
from sodatoon.permissions import IsArtist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class EpisodeLikeViewSet(viewsets.ModelViewSet):
    queryset = EpisodeLike.objects.all().order_by('id')
    serializer_class = EpisodeLikesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]