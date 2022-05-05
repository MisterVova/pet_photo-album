from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from ..serializers import PhotoSerializer, Photo, PhotoUpdateSerializer


class PhotoViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   # mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # print("==PhotoSerializer ==",repr(PhotoSerializer()))
        user = self.request.user
        items = Photo.objects.filter(user=user)
        return items

    # def perform_create(self, serializer:PhotoSerializer):
    #     # print("user", self.request.user)
    #     album = serializer.validated_data.get("album",)
    #
    #     # print("album", album)
    #     # print("album", album.user)
    #     # print("user", serializer.validated_data.get("user",))
    #     # print("request.user", self.request.user)
    #     # if (serializer.validated_data.)
    #     # if (album.user !=self.request.user) : serializer.ValidationError("aaaaa")
    #     # from rest_framework import serializers
    #     # if album.user !=self.request.user :
    #     #     raise serializers.ValidationError("aaaaa")
    #
    #     serializer.save(user=self.request.user)

    # def create(self, request):
    #
    #     # serializer = PhotoSerializer(data=request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     # return Response({'post': serializer.data})
    #     return super.create(request)

    #     def update(self, request, pk=None):
    #         Tag.get_context(request=request)
    #         if not pk:
    #             return Response({"error": "Method PUT not allowed"})
    #
    #         try:
    #             instance = Tag.objects.get(pk=pk)
    #         except:
    #             return Response({"error": "Object does not exists"})
    #
    #         serializer = TagSerializer(data=request.data, instance=instance)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response({"tag": serializer.data})


class PhotoUpdateViewSet(mixins.UpdateModelMixin,
                         # mixins.RetrieveModelMixin,
                         # mixins.ListModelMixin,
                         GenericViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        items = Photo.objects.filter(user=user)
        return items
