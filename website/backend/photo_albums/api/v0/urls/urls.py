from rest_framework import routers
from photo_albums.api.v0.views import TagViewSet, PhotoViewSet, AlbumViewSet, ImageViewSet, ImageSmallViewSet

router = routers.DefaultRouter()
urlpatterns = [
]

router.register('tags', TagViewSet)
router.register('photo', PhotoViewSet)
router.register('albums', AlbumViewSet)
router.register('image', ImageViewSet)
router.register('image-small', ImageSmallViewSet)

urlpatterns += router.urls
