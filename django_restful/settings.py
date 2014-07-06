"""
Settings for the django_restful app
"""

from django.conf import settings
from django_restful import constants

DJANGO_RESTFUL_FORCE_LANGUAGE = getattr(
    settings,
    'DJANGO_RESTFUL_FORCE_LANGUAGE',
    constants.DJANGO_RESTFUL_FORCE_LANGUAGE
)

DJANGO_RESTFUL_DEFAULT_LANGUAGE = getattr(
    settings,
    'DJANGO_RESTFUL_DEFAULT_LANGUAGE',
    constants.DJANGO_RESTFUL_DEFAULT_LANGUAGE
)
