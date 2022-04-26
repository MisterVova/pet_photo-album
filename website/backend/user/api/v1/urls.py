from rest_framework import routers

from user.api.v1.views import UserViewSet
from django.urls import path, include, re_path

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
]

router = routers.DefaultRouter()
router.register('signup', UserViewSet)

urlpatterns += router.urls
