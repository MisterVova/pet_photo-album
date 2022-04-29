from rest_framework import viewsets
from ..serializers import PhotoSerializer, Photo


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
