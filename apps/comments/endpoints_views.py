from apps.comments.models import Comments
from apps.comments.serializers import CommentsSerializer
from sodatoon.permissions import IsArtist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtist]