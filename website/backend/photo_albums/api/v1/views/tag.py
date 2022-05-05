from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from ..serializers import TagSerializer, Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser,)

    # def get_queryset(self):
    #     user = self.request.user
    #     print(user)
    #     list = Tag.objects.filter(user=user)

# class TagViewSet2(viewsets.ViewSet):
#     # queryset = Tag.objects.all()
#     # serializer_class = TagSerializer
#     # permission_classes = (IsAdminUser,)
#     # def dispatch(self, request, *args, **kwargs):
#     #     print("TagViewSet",self, request, *args, **kwargs,sep="\n")
#     #     pass
#     def get(self,request):
#         """Что то особенное """
#         Tag.get_context()
#         Tag.objects.all(request)
#         t = Tag.objects.all()
#         return Response({"tags": TagSerializer(t, many=True).date})
#         # def pos
#         # def pu
#         # def patc
#         # def __delete__(self, instance):
#         """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.
#
#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """
#
#     # @swagger_auto_schema(request_body=TagSerializer)
#     def list(self, request):
#         Tag.get_context(self,request=request)
#         t = Tag.objects.all()
#         return Response({"tags": TagSerializer(t, many=True).data})
#
#     # @swagger_auto_schema(request_body=TagSerializer)
#     def create(self, request):
#         Tag.get_context(request=request)
#         serializer = TagSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     # @swagger_auto_schema(request_body=TagSerializer)
#     def retrieve(self, request, pk=None):
#         Tag.get_context(request=request)
#
#         # if not pk:
#         #     return Response({"error": "Method retrieve not allowed"})
#
#         try:
#             tag = Tag.objects.get(pk=pk)
#             if tag:
#                 return Response({"tag": TagSerializer(tag).data})
#         except:
#             pass
#         #
#         # if tag:
#         #     return Response({"tag": TagSerializer(tag).data})
#         return Response({"error": "Object does not exists"})
#
#     # @swagger_auto_schema(request_body=TagSerializer)
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
#
#     # @swagger_auto_schema(request_body=TagSerializer)
#     def partial_update(self, request, pk=None):
#         Tag.objects.all(request)
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
#
#     # @swagger_auto_schema(request_body=TagSerializer)
#     def destroy(self, request, pk=None):
#         Tag.objects.all(request)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         # здесь код для удаления записи с переданным pk
#         tag = Tag.objects.get(pk=pk)
#         tag.delete()
#         return Response({"post": "delete post " + str(pk)})


#
# class TagAPIView(APIView):
#     serializer_class = TagSerializer
#
#     def get(self, request):
#         print("Tag get_context request.method=", request.method)
#         movie_id = request.query_params.get('movie', None)
#
#         if movie_id:
#             movies = Tag.objects.filter(movie_id=movie_id)
#         else:
#             movies = Tag.objects.all()
#
#         if movies:
#             movie_serializer = self.serializer_class(movies, many=True)
#             return Response(movie_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'No movies found'}, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         print("Tag get_context request.method=", request.method)
#         title = request.data.get('title', None)
#         description = request.data.get('description', None)
#         category = request.data.get('category', 'Cartoon')
#
#         post_data = {
#             'title': title,
#             'description': description,
#             'category': category
#         }
#
#         serializer = self.serializer_class(data=post_data)
#         if serializer.is_valid(raise_exception=True):
#             movie = serializer.save()
#
#         if movie:
#             return Response({'message': 'Successful new movie'}, status=status.HTTP_201_CREATED)
#         return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request):
#         print("Tag get_context request.method=", request.method)
#         movie_id = request.query_params.get('movie', None)
#
#         movie = Tag.objects.get(movie_id=movie_id)
#
#         if not movie:
#             return Response({'message': 'No movies found'})
#
#         title = request.data.get('title', None)
#         if title:
#             movie.title = title
#             movie.save()
#
#         description = request.data.get('description', None)
#         if description:
#             movie.description = description
#             movie.save()
#
#         category = request.data.get('category', None)
#         if category:
#             movie.category = category
#             movie.save()
#
#         return Response({'message': 'Update Complete'}, status=status.HTTP_200_OK)
#
#     def delete(self, request):
#         print("Tag get_context request.method=", request.method)
#         movie_id = request.query_params.get('movie', None)
#         movie = Tag.objects.get(movie_id=movie_id)
#
#         if not movie:
#             return Response({'message': 'No movie found'}, status=status.HTTP_404_NOT_FOUND)
#
#         movie.delete()
#         return Response({'message': 'Movie removed'}, status=status.HTTP_200_OK)

# https://overcoder.net/q/475368/%D0%BA%D0%B0%D0%BA-%D0%B2%D0%B5%D1%80%D0%BD%D1%83%D1%82%D1%8C-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2-%D1%81-%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC-%D0%BF%D0%BE%D0%BB%D0%B5%D0%BC-%D0%B2-json-django-rest-framework
# class CustomPageNumberPagination(PageNumberPagination):
#
#     def get_paginated_response(self, data, total_time):
#         return Response(OrderedDict([
#             ('count', self.page.paginator.count),
#             ('next', self.get_next_link()),
#             ('previous', self.get_previous_link()),
#             ('total_time', total_time),
#             ('results', data)
#         ]))
