from .base import *
from django.contrib.messages import constants as messages

SECRET_KEY = 'django-insecure-+3g4(hk#wx@(qa8t=08t1)l3ex3g!mglj$pps7%fe4&ssq^0fo'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'fb7af650e0d76f'
EMAIL_HOST_PASSWORD = 'a9c375d578545b'
EMAIL_PORT = '2525'