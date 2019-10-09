#import core.py script
from .core import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'messenger',
        'USER': 'postgres',
        'PASSWORD': 'unicesmag',
        'HOST': 'localhost',
        'PORT': '5432', #Empty->Default: 5432
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')