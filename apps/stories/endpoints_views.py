from apps.stories.serializers import StorySerializer
from apps.stories.models import Story
from sodatoon.permissions import IsArtist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('id')
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]