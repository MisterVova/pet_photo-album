from rest_framework import serializers
from photo_albums.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        ref_name = "TagSerializer V0"
