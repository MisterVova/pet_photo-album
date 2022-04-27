from rest_framework import viewsets
from photo_albums.api.v1.serializers import TagSerializer, Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
