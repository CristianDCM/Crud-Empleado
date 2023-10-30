import os
from .base import *
import pymysql

pymysql.version_info = (1, 4, 6, 'final', 0)
pymysql.install_as_MySQLdb()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-qkolk5%+eeu(8znqs2r+10^&(igly7!bi)6qmvzq21e+$y$vuq"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'empleadopro',
        "USER": 'root',
        "PASSWORD": '',
        "HOST": 'localhost',
        "PORT": '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder',
                          'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                          'compressor.finders.CompressorFinder',)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

STATIC_URL = "static/"
STATICFILES_DIRS = [
 "static/",
]

MEDIA_URL = "/media/"
MEDIA_DIR = BASE_DIR / "media"
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = "/media/"