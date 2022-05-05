from django.urls import path
from rest_framework import routers
from photo_albums.api.v1.views import TagViewSet, PhotoViewSet, AlbumViewSet, PhotoUpdateViewSet
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

# from photo_albums.api.v1.views.tag import TagViewSet2

router = routers.DefaultRouter()
urlpatterns = [
    # path('tags2/', TagViewSet2.as_view({'get': 'list'}))
    # path('movies/', TagAPIView.as_view()),
]

router.register('tags', TagViewSet)
router.register('albums', AlbumViewSet)
router.register('photo', PhotoViewSet)
router.register('photo/edit', PhotoUpdateViewSet)

# router.register('tags2', TagViewSet2, basename='tag')
# router.register('tags2', TagViewSet2)
# router.register('image', ImageViewSet)
# router.register('image-small', ImageSmallViewSet)


urlpatterns += router.urls

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Dummy API",
#         default_version='v1',
#         description="Dummy description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@dummy.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
#
# urlpatterns += [
#     # url(r'^playground/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     # path('swagger/',
#     #      swagger_schema_view.with_ui('swagger', cache_timeout=0),
#     #      name='schema-swagger-ui'
#     #      ),
#     # path('redoc/',
#     #      swagger_schema_view.with_ui('redoc', cache_timeout=0),
#     #      name='schema-redoc'
#     #      ),
#     path('api_schema/', get_schema_view(
#         title='API Schema',
#         description='Guide for the REST API'
#     ), name='api_schema'),
# ]


urlpatterns = [path('api_schema/', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
               path('docs/', TemplateView.as_view(template_name='docs.html', extra_context={'schema_url': 'api_schema'}), name='swagger-ui'),
               ] + urlpatterns
