from rest_framework import viewsets
from photo_albums.api.v1.serializers import ImageSmallSerializer, ImageSmall


class ImageSmallViewSet(viewsets.ModelViewSet):
    queryset = ImageSmall.objects.all()
    serializer_class = ImageSmallSerializer
