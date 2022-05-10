from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializers import AlbumSerializer, Album


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        # print(user)
        items = Album.objects.filter(user=user)
        return items
    #
    # def create(self, request):
    #     serializer = AlbumSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
