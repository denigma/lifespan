# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lal^$i3gh=qv&ge9-8ai1kld_32=c4e7%#a_i2s_w(b_fbh6^('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}


if os.path.exists(os.path.join(PROJECT_ROOT, 'local_settings.py')):
    BACKEND = 'mysql'
else:
    BACKEND = 'sqlite3'

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/" #'http://localhost/static/'

folders = ["static","coffee","styles","resources","media","libs"]
de_apps = ['media','annotations']
apps = ["lifespan","tables","chats","grids"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reversion',
    'rest_framework',
    'rest_framework_swagger',
    'south',
    'coffeescript',
    'less',
    'django_filters',
    'easy_pjax',
    'bulbs',
    ] + de_apps + apps


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'lifespan.disable.DisableCSRF', #DISABLE THIS ANNOYING CSRF
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS = (#
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'pinax_utils.context_processors.settings',
)#


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'coffeescript.finders.CoffeescriptFinder',
    'less.finders.LessFinder',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    )

}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
APPEND_SLASH = True

COFFEESCRIPT_MTIME_DELAY = 1
COFFEESCRIPT_OUTPUT_DIR = "js"

LESS_MTIME_DELAY = 1
LESS_OUTPUT_DIR = "css"


# Additional locations of static files
STATICFILES_DIRS = [a + str("/") + f for f in folders for a in apps] + [f for f in folders if f!="static"]

ROOT_URLCONF = 'lifespan.urls'

WSGI_APPLICATION = 'lifespan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [a + "/templates" for a in apps]