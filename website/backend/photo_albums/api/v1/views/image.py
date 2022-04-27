from rest_framework import viewsets
from photo_albums.api.v1.serializers import ImageSerializer, Image


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
