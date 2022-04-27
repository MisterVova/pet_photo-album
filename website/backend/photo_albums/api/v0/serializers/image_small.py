from rest_framework import serializers
from photo_albums.models import ImageSmall


class ImageSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSmall
        fields = "__all__"