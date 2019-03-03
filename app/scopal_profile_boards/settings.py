"""
Django settings for scopal_profile_boards project.

Author: __other__ <ministry@scopal-affairs.com>
created on: June 25 2018

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4tr^w6d5vu%m4*8&wnjxt%k62&0t)039&2-p)(#=pcmgs#&ir7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #cms
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    # boards
    'django.contrib.humanize',
    'widget_tweaks',
    'interface',
    'accounts',
    'boards',
    # frontend coupling
    'webpack_loader',
    # rest
    'rest_framework',
    'rest_framework.authtoken',
    'api',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # CMS Middleware
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
]

ROOT_URLCONF = 'scopal_profile_boards.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # CMS
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'scopal_profile_boards.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pgdb',
        'USER': 'pguser',
        'PASSWORD': 'pguser',
        'HOST': 'db',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

ALLOWED_HOSTS = ['*']

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CMS Languages
LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
]

CMS_TEMPLATES = [
    ('home.html', 'Home page template'),
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'interface/static/dist'),
]

# Frontend Dependencies
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

# Redirects
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Twitter API
TWITTER_FEED_CONSUMER_PUBLIC_KEY = 'fZ9FP2PGobeRZEXyaHM2x1SmX'
TWITTER_FEED_CONSUMER_SECRET = '2il1cyCprSczx7ySt09h4WaA4SwY9B77z4iFai3Dn4bEfPG1kg'
TWITTER_FEED_OPEN_AUTH_TOKEN = '767624817956757504-yOTiKj6axNjVNor66Wu4lp0fGRAagwk'
TWITTER_FEED_OPEN_AUTH_SECRET = 'Ix9ezLOq8T7YBhTrsCBGWUwZx34z78P4vvw683xKVg2NJ'
