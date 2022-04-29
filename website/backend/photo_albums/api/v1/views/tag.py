from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from ..serializers import TagSerializer, Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser,)


class TagViewSet2(viewsets.ViewSet):
    # queryset = Tag.objects.all()
    # serializer_class = TagSerializer
    # permission_classes = (IsAdminUser,)
    # def dispatch(self, request, *args, **kwargs):
    #     print("TagViewSet",self, request, *args, **kwargs,sep="\n")
    #     pass
    def get(self):
        t = Tag.objects.all()
        return Response({"tags": TagSerializer(t, many=True).date})
        # def pos
        # def pu
        # def patc
        # def __delete__(self, instance):
        """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    @swagger_auto_schema(request_body=TagSerializer)
    def list(self, request):
        t = Tag.objects.all()
        return Response({"tags": TagSerializer(t, many=True).data})

    @swagger_auto_schema(request_body=TagSerializer)
    def create(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    @swagger_auto_schema(request_body=TagSerializer)
    def retrieve(self, request, pk=None):

        # if not pk:
        #     return Response({"error": "Method retrieve not allowed"})

        try:
            tag = Tag.objects.get(pk=pk)
            if tag:
                return Response({"tag": TagSerializer(tag).data})
        except:
            pass
        #
        # if tag:
        #     return Response({"tag": TagSerializer(tag).data})
        return Response({"error": "Object does not exists"})

    @swagger_auto_schema(request_body=TagSerializer)
    def update(self, request, pk=None):
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Tag.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = TagSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"tag": serializer.data})

    @swagger_auto_schema(request_body=TagSerializer)
    def partial_update(self, request, pk=None):
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Tag.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = TagSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"tag": serializer.data})

    @swagger_auto_schema(request_body=TagSerializer)
    def destroy(self, request, pk=None):
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        # здесь код для удаления записи с переданным pk
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response({"post": "delete post " + str(pk)})
