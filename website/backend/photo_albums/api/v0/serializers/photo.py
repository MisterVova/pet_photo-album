from rest_framework import serializers
from photo_albums.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
        ref_name = "PhotoSerializer V0"
