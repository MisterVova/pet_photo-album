from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializers import AlbumSerializer, Album

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)

    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['album', 'tags',]
    search_fields = ['name']
    ordering_fields = ['created_at', 'count']
    ordering = ['created_at']

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

    # def get_queryset(self):
    #     user = self.request.user
    #     items = Album.get_queryset_by_request(request=self.request, user=user)
    #     return items
