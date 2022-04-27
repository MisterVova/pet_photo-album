from garpixcms.urls import *  # noqa

urlpatterns = [
                  path('api/v0/user/', include('user.api.v0.urls')),
                  # path('drf-auth/', include('rest_framework.urls')),
                  path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                  path('api/v0/service/', include('photo_albums.api.v0.urls')),
              ] + urlpatterns  # noqa
