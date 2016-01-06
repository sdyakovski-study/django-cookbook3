"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# settings.py will be read and evaluated on the project level (possibly by manage.py).
# BASE_DIR points to the '/home/sdyakovski/projects/python-projects/django-cookbook/project'
# but is dealing with relative paths, not absolute paths, so its value from manage.py would be ''.
# It simply starts with __file__ (which is settings.py); its dirname (myproject); and its dirname (project),
# which is the curdir of manage.py => '' 

# ADD EXTERNALS PATHS TO sys.path
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# BASE_PATH is abspath of 'myproject/..', which is 
# '/home/sdyakovski/projects/python-projects/django-cookbook/project'
# - which is the same dir as BASE_DIR, but absolute (needed for sys.path)
EXTERNAL_LIBS_PATH = os.path.join(BASE_PATH, 'externals', 'libs')
EXTERNAL_APPS_PATH = os.path.join(BASE_PATH, 'externals', 'apps')
sys.path = ['', EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path[1:]
# [1:] in order to eliminate the first element of the list (''), which is moved to the front
print sys.path

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# PROJECT_PATH is abspath of 'myproject', where __file__ (settings.py) is, which is 
# '/home/sdyakovski/projects/python-projects/django-cookbook/project/myproject'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p!etd25ic9l6d-i3m2h*6_u8eul69m)%68#@xl#^tfnd%w3g0n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOCALE_PATHS = (
    os.path.join(BASE_PATH, 'locale'),
)

# Media files location - uploaded by users?
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# Static files location
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# Static files (CSS, JavaScript, Images) served by the server ?
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'site_static'),
)

# Templates location
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

# File Upload Temp location
FILE_UPLOAD_TEMP_DIR = os.path.join(PROJECT_PATH, 'tmp')33