from rest_framework import serializers
from photo_albums.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
        ref_name = "AlbumSerializer V0"
