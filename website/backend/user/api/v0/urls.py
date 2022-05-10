from rest_framework import routers
from user.api.v0.views import UserViewSet
# from django.urls import path, include

urlpatterns = [

]

router = routers.DefaultRouter()
router.register('signup', UserViewSet)
urlpatterns += router.urls
