from rest_framework import viewsets
from ..serializers  import AlbumSerializer, Album


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
