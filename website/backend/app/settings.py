from garpixcms.settings import *  # noqa
from garpixcms.settings import INSTALLED_APPS  # noqa
from garpixcms.settings import REST_FRAMEWORK  # noqa

DEFAULT_AUTHENTICATION_CLASSES = list(REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"])
DEFAULT_AUTHENTICATION_CLASSES += [
    # 'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
]

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = DEFAULT_AUTHENTICATION_CLASSES

LOGIN_URL = '/admin/login/'

INSTALLED_APPS += [
    "photo_album",
    "photo_albums",  # old
    'drf_yasg',
    "rest_framework_swagger",
]
