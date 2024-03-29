"""""
Django settings for newtest project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv,dotenv_values
import os
import logging
import datetime
# load_dotenv()
temp = dotenv_values(".env")
DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
print(DJANGO_SECRET_KEY)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'djbkbz+bu*a&+hq((@wr+48438u=i#8ip#p!my5j2*eti#0u)d'

SECRET_KEY = 'qj8may(ldb_&zu$ne6t4%(!(u4xia*a+%ud4%+s@*&+ywl+)6c'
# SECRET_KEY = os.getenv("SECRET_KEY") 
# SECRET_KEY = temp["SECRET_KEY"]


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG = True
# ALLOWED_HOSTS = ["*","sbsy.co.in","www.sbsy.co.in","103.129.97.81"]
ALLOWED_HOSTS = ['*', 'sbsy.co.in','www.sbsy.co.in',"103.129.97.81","http://localhost/","http://sbsy.co.in:8000/","https://ad53-157-119-80-37.in.ngrok.io/"]
CSRF_TRUSTED_ORIGINS = ['https://your-domain.com', 'https://www.your-domain.com',"https://ad53-157-119-80-37.in.ngrok.io","https://aa6e-157-119-80-37.in.ngrok.io"]

# Application definition


INSTALLED_APPS = [
    #  'adminlte3',
    #   'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
     'school',
     'lybrary',
      'django_cleanup',
      'online_users',
      'social_django', # add this social
      'core', # add this
     
]



#add this
AUTHENTICATION_BACKENDS = [
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]


# MIDDLEWARE_CLASSES = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'online_users.middleware.OnlineNowMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
# ]


ROOT_URLCONF = 'newsbsy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', # add this
                'social_django.context_processors.login_redirect', # add this
            ],
        },
    },
]

WSGI_APPLICATION = 'newsbsy.wsgi.application'


#SECURE_SSL_REDIRECT = True


# WSGI_APPLICATION = 'newtest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / '../newsbsyDb/db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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




SOCIAL_AUTH_FACEBOOK_KEY = 'xxxxxxxxxxxxxxxxxxxx'        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'xxxxxxxxxxxxxxxxxxxx' # App Secret
SOCIAL_AUTH_FACEBOOK_KEY = "922407651688981"
SOCIAL_AUTH_FACEBOOK_SECRET = "e0c732567e6a9370c50b7ae06a442f8e"
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
  'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]


# add this code
SOCIAL_AUTH_INSTAGRAM_KEY = 'xxxxxxxxxxxxxxxxxxxx'         #Client ID
SOCIAL_AUTH_INSTAGRAM_SECRET = 'xxxxxxxxxxxxxxxxxxxx'  #Client SECRET
SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = [               
    ('user', 'user'),
]


SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '8644awg3etpd93'         #Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'ekqgX4vRuhKLAYn4'  #Client Secret
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'formatted-name', 'public-profile-url', 'picture-url']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
    ('id', 'id'),
    ('formattedName', 'name'),
    ('emailAddress', 'email_address'),
    ('pictureUrl', 'picture_url'),
    ('publicProfileUrl', 'profile_url'),
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATIC_URL = '/static/'
# # STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL='/media/'
# MEDIA_ROOT=os.path.join(BASE_DIR,'media')


# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# #STATIC_ROOT=os.path.join(BASE_DIR,"/static/")                # comment STATICFILES_DIRS and uncomment STATIC_ROOT for python manage.py collectstatic  make DEBUG = True then runserver


# import os
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

if not DEBUG:
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS=True
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_PORT=2253
    EMAIL_HOST_USER='alokraj.ad@gmail.com'
    DEFAULT_FROM_EMAIL='alokraj.ad@gmail.com'
    SERVER_EMAIL='alokraj.ad@gmail.com'
    EMAIL_HOST_PASSWORD='mummadaida'
else:
    EMAIL_BACKEND=('django.core.mail.backends.console.EmailBackend')


# LOGIN_URL = 'login1'
# LOGIN_REDIRECT_URL = 'home1'
# LOGOUT_URL = 'logout1'
# LOGOUT_REDIRECT_URL = 'login1'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'

# DataFlair #Logging Information


LOGGING = {
'version': 1,
'disable_existing_loggers': True,

'formatters': {

    'standard': {
        'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    },
},

'handlers': {
    'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/newsbsy/sbsy-debug.log',
            'formatter': 'standard',
        },
    'default': {
        'level':'INFO',
        'class':'logging.handlers.RotatingFileHandler',
        'filename': os.path.join(BASE_DIR, 'log/newsbsy/sbsy-debug.log'),
        'maxBytes': 1024*1024*5, # 5 MB
        'backupCount': 5,
        'formatter':'standard',
    },
    'logfile': {
        'level': 'INFO',
        'class': 'logging.FileHandler',
        'filename': os.path.join(BASE_DIR, 'log/newsbsy/debug.log'),
    },
},

'loggers': {
    'django.request': {
        'handlers': ['default'],
        'level': 'INFO',
        'propagate': True,
    },
    # 'django.request': {
    #     'handlers': ['logfile'],
    #     'level': 'WARNING',
    #     'propagate': True,
    # },
    '': {
        'handlers': ['default'],
        'level': 'INFO',
        'propagate': True,
    },
}

}

DEFAULT_AUTO_FIELD='django.db.models.AutoField'



try:
    from .nginx_settings import *
except ImportError:
    pass