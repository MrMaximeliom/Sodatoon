from apps.storyLikes.serializers import StorySerializer
from apps.storyLikes.models import StoryLike
from sodatoon.permissions import IsArtist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class StoryLikesViewSet(viewsets.ModelViewSet):
    queryset = StoryLike.objects.all().order_by('id')
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]