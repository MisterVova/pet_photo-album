from garpixcms.settings import *  # noqa

DEFAULT_AUTHENTICATION_CLASSES = list(REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"])
DEFAULT_AUTHENTICATION_CLASSES += [
    # 'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
]

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = DEFAULT_AUTHENTICATION_CLASSES

LOGIN_URL = '/admin/login/'

INSTALLED_APPS += [
    "photo_albums",
]
