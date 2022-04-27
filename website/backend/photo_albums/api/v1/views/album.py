from rest_framework import viewsets
from photo_albums.api.v1.serializers import AlbumSerializer, Album


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
