from django.urls import path
from rest_framework import routers
from photo_album.views import TagViewSet, PhotoViewSet, AlbumViewSet
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

# from photo_albums.api.v1.views.tag import TagViewSet2


router = routers.DefaultRouter()
urlpatterns = [
]

router.register('tags', TagViewSet)
router.register('albums', AlbumViewSet)
router.register('photo', PhotoViewSet)
# router.register('photo/update', PhotoUpdateViewSet)

urlpatterns += router.urls

urlpatterns = [path('api_schema/', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
               path('docs/', TemplateView.as_view(template_name='docs.html', extra_context={'schema_url': 'api_schema'}), name='swagger-ui'),
               ] + urlpatterns
