"""
Django settings for dev_cms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'chu=6^+1__%xy3&kg9h(4$1cz@mct(i*_fo8cbjc-)pg9_jnvi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", ]


# Application definition

INSTALLED_APPS = (
    'django_ace',

    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'reversion',
    'django_summernote',
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
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'dev_cms.urls'

WSGI_APPLICATION = 'dev_cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_cms',
        'USER': 'postgres',
        'PASSWORD': 'password',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.request',
    )


from django.conf.global_settings import TEMPLATE_LOADERS

TEMPLATE_LOADERS = (
        'dev_cms.loader.DBTemplateLoader',
    ) + TEMPLATE_LOADERS


# Admin-tools files
ADMIN_TOOLS_MENU = 'menu.CMSMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CMSIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dashboard.CMSAppIndexDashboard'

POSTS_PREFIX = 'blog'
POST_LIST_TEMPLATE = 'list.html'
POST_CATEGORY_LIST_TEMPLATE = 'category_list.html'
POST_DETAIL_TEMPLATE = 'detail.html'
POSTS_PER_PAGE = 10

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''

if not DEBUG:
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


SUMMERNOTE_CONFIG = {
    'width': 720,
    'height': 480,
    'toolbar': [
        ['style', ['style']],
        ['font', ['bold', 'italic', 'underline', 'clear']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video']],
        ['misc', ['codeview']]
    ],
    'attachment_upload_to': 'uploaded_filepath',
    'attachment_storage_class': None,
    'attachment_filesize_limit': 1024 * 1024,
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

FILER_DEBUG = DEBUG
FILER_ENABLE_LOGGING = True
