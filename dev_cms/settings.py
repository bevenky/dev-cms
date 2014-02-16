from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, TEMPLATE_LOADERS, MEDIA_ROOT

from import_export.formats import base_formats

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", ]


# Application definition

INSTALLED_APPS = (
    'django_ace',
    'ckeditor',
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'reversion',
    'storages',
    'easy_thumbnails',
    'filer',
    'import_export',
    'fack',

    'appearance',
    'pages',
    'redirects',
    'posts',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'dev_cms.urls'

WSGI_APPLICATION = 'dev_cms.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_TZ = True

USE_I18N = False

USE_L10N = False

APPEND_SLASH = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.request',
    )

TEMPLATE_LOADERS = (
        'dev_cms.loader.DBTemplateLoader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ) + TEMPLATE_LOADERS

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Dev-CMS',

    # misc
    'LIST_PER_PAGE': 50
}

if not DEBUG:
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# ckeditor related config
CKEDITOR_UPLOAD_PATH = "static_media"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Full': [
        ['Format', 'Bold', 'Italic', 'Underline', 'Strike'],
        ['Blockquote', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', ],
        ['NumberedList', 'BulletedList'],
        ['Image', 'Table', 'HorizontalRule'],
        ['TextColor', 'BGColor'], ['Link', 'Unlink', 'Anchor'], ['Maximize','Source'],
        ],
        'toolbar': 'Full',
        'height': 500,
        'width': 750,
        'scayt_autoStartup': 'true',
    },
}

# filer related config - used by media uploads
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

FILER_DEBUG = DEBUG
FILER_ENABLE_LOGGING = True
FILER_STORAGES = { 'public': { 'main': { 'UPLOAD_TO_PREFIX': 'assets'} } }

# import - export - formats
IMPORT_EXPORT_FORMATS = (base_formats.JSON,)


# dev-cms config below

## posts config
POSTS_URL_PREFIX = 'blog'
POSTS_TEMPLATE_PREFIX = 'blog'
POST_LIST_TEMPLATE = 'list.html'
POST_CATEGORY_LIST_TEMPLATE = 'category_list.html'
POST_AUTHOR_LIST_TEMPLATE = 'author_list.html'
POST_DETAIL_TEMPLATE = 'detail.html'
POSTS_PER_PAGE = 10
POPULAR_POSTS = 7

try:
    from .custom_settings import *
except ImportError:
    pass

