"""
Django settings for lifespan project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
print(BASE_DIR)
print(PACKAGE_ROOT)
print(BASE_DIR == PACKAGE_ROOT)

# from gears.environment import Environment
# from gears.finders import FileSystemFinder
#
# from gears_coffeescript import CoffeeScriptCompiler

# ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
# ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
# STATIC_DIR = os.path.join(ROOT_DIR, 'static')
#
# env = Environment(STATIC_DIR)
# env.finders.register(FileSystemFinder([ASSETS_DIR]))
# env.register_defaults()
# env.compilers.register('.coffee', CoffeeScriptCompiler.as_handler())


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lal^$i3gh=qv&ge9-8ai1kld_32=c4e7%#a_i2s_w(b_fbh6^('

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
    'coffeescript',
    'less',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS = (#
    'django.contrib.auth.context_processors.auth',#
    'django.core.context_processors.debug',#
    'django.core.context_processors.i18n',#
    'django.core.context_processors.media',#
    'django.core.context_processors.static',#
    'django.core.context_processors.request',
    'pinax_utils.context_processors.settings',
)#


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'coffeescript.finders.CoffeescriptFinder',
    'less.finders.LessFinder',
)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


COFFEESCRIPT_MTIME_DELAY = 1
COFFEESCRIPT_OUTPUT_DIR = "./static/js"

LESS_MTIME_DELAY = 1
LESS_OUTPUT_DIR = "./static/css"



# Additional locations of static files
STATICFILES_DIRS = (
    "static",
)


ROOT_URLCONF = 'lifespan.urls'

WSGI_APPLICATION = 'lifespan.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    'templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
