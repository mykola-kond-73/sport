from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-j!e09-^=j00yjhzt_h$yb_se2rkw88&^m0nm_aes+io^y_2k#c'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'sport.apps.SportConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coolcite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coolcite.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS =[

]

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    "127.0.0.1",
]


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR,'coolsite_cache'),
    }
}


LOGGING={
    'version': 1,
    'disable_existing_loggers': False,

    'formatters':{
        'error_formatter':{
            'format':"[{asctime}] - [{levelname}] - {module} - {filename} - {lineno} -- {message}",
            'style':'{'
        },
        'info_formatter':{
            'format':"[{asctime}] - [{levelname}] - {module} - {filename} -- {message}",
            'style':'{'

        }
    },

    'handlers':{
        'error_handler':{
            'class':'logging.FileHandler',
            'formatter':'error_formatter',
            'filename':os.path.join(BASE_DIR, 'logs/error.log'),
            'encoding': 'utf-8'
        },
        'info_handler':{
            'class':'logging.FileHandler',
            'formatter':'info_formatter',
            'filename': os.path.join(BASE_DIR, 'logs/info.log'),
            'encoding': 'utf-8'
        }
    },

    'loggers':{
        'error_logger':{
            'handlers':['error_handler'],
            'level':'ERROR',
            'propagate':True
        },
        'info_logger':{
            'handlers':['info_handler'],
            'level':'INFO',
            'propagate':True
        }
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'