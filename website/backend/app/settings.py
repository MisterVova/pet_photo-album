from garpixcms.settings import *  # noqa
from garpixcms.settings import INSTALLED_APPS  # noqa
from garpixcms.settings import REST_FRAMEWORK  # noqa

# DEFAULT_AUTHENTICATION_CLASSES = list(REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"])
DEFAULT_AUTHENTICATION_CLASSES = []
DEFAULT_AUTHENTICATION_CLASSES += [
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
]

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = DEFAULT_AUTHENTICATION_CLASSES

REST_FRAMEWORK['DEFAULT_FILTER_BACKENDS'] = ['django_filters.rest_framework.DjangoFilterBackend']

LOGIN_URL = '/admin/login/'

INSTALLED_APPS += [
    "photo_album",
    'drf_yasg',
    "rest_framework_swagger",
    # 'rest_framework.authtoken',
    'djoser',
    "django_filters",
]

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {},
}
