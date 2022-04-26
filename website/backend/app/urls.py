from garpixcms.urls import *  # noqa


urlpatterns = [
                  path('api/v1/user/', include('user.api.v1.urls')),
                  # path('drf-auth/', include('rest_framework.urls')),
                  path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
              ] + urlpatterns  # noqa