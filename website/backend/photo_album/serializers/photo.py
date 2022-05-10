from rest_framework import serializers

from photo_album.models import Photo


class ImageInfoSerializer(serializers.Serializer):
    # path = serializers.CharField(read_only=True)
    # name = serializers.CharField(read_only=True)
    url = serializers.CharField(read_only=True)
    # uri = serializers.CharField()
    width = serializers.IntegerField(read_only=True)
    height = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class PhotoSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True, source='user.id')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image_info = ImageInfoSerializer(read_only=True, source="image", )
    image_small_info = ImageInfoSerializer(read_only=True, source="image_small", )

    class Meta:
        model = Photo
        exclude = ("updated_at",)
        read_only_fields = ['image_small']
        # validators = [
        #     PhotoValidator(
        #         queryset_album=Album.objects.all(),
        #         queryset_photo=Photo.objects.all(),
        #         # fields=['list', 'position']
        #     )
        # ]


class PhotoUpdateSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):
        read_only_fields = ['image_small', "image"]


class PhotoFilterSerializer(serializers.Serializer):
    album_id = serializers.ListField(child=serializers.IntegerField(min_value=1), allow_empty=True, min_length=None, max_length=None, default=[])
    tag_id = serializers.ListField(child=serializers.IntegerField(min_value=1), allow_empty=True, min_length=None, max_length=None, default=[])
    album_name = serializers.ListField(child=serializers.CharField(), allow_empty=True, min_length=None, max_length=None, default=[])
    tag_name = serializers.ListField(child=serializers.CharField(), allow_empty=True, min_length=None, max_length=None, default=[])
    ordering = serializers.ListField(child=serializers.CharField(), allow_empty=True, min_length=None, max_length=None, default=[])

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
