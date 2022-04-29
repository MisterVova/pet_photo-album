from garpixcms.urls import *  # noqa
from rest_framework.schemas import get_schema_view

urlpatterns = [
                  path('api/v0/user/', include('user.api.v0.urls')),
                  # path('drf-auth/', include('rest_framework.urls')),
                  path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                  path('api/v0/service/', include('photo_albums.api.v0.urls')),
                  path('api/v1/service/', include('photo_albums.api.v1.urls')),
                  # path('api_schema/', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
              ] + urlpatterns  # noqa

# urlpatterns = [
#                   path('api_schema/', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
#               ] + urlpatterns
