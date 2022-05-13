from rest_framework import serializers
from photo_album.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # user = serializers.CurrentUserDefault()
    # user = serializers.CharField(read_only=True)
    # user = serializers.IntegerField(source="user.id", read_only=True)
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True, source='user.id')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(read_only=True)
    count = serializers.IntegerField(read_only=True, source='photos.count')

    # def create(self, validated_data):
    #     # print("zzzzz", validated_data)
    #     # validated_data["user"]=validated_data
    #     return Album.objects.create(**validated_data)


    class Meta:
        model = Album
        # fields = "__all__"
        # fields = "__all__"
        exclude = ("updated_at",)


class AlbumFilterSerializer(serializers.Serializer):
    ordering = serializers.ListField(child=serializers.CharField(), allow_empty=True, min_length=None, max_length=None, default=[])

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
