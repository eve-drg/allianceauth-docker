# Every setting in base.py can be overloaded by redefining it here.
from .base import *

# Django App Secretkey change if you want
SECRET_KEY = 'REPLACETHISSHIT'

# Change this to change the name of the auth site
SITE_NAME = 'Alliance Auth'

DEBUG = False
# Add any additional apps to this list. Pre-Populated with some Apps
INSTALLED_APPS += [
'allianceauth.services.modules.discord',
'allianceauth.services.modules.teamspeak3',
]
# Teamspeak3 Configuration
TEAMSPEAK3_SERVER_IP = '127.0.0.1'
TEAMSPEAK3_SERVER_PORT = 10011
TEAMSPEAK3_SERVERQUERY_USER = 'serveradmin'
TEAMSPEAK3_SERVERQUERY_PASSWORD = ''
TEAMSPEAK3_VIRTUAL_SERVER = 1
TEAMSPEAK3_PUBLIC_URL = ''

CELERYBEAT_SCHEDULE['run_ts3_group_update'] = {
    'task': 'allianceauth.services.modules.teamspeak3.tasks.run_ts3_group_update',
    'schedule': crontab(minute='*/30'),
}
# Discourse Configuration
DISCOURSE_URL = ''
DISCOURSE_API_USERNAME = ''
DISCOURSE_API_KEY = ''
DISCOURSE_SSO_SECRET = ''

# SMF Configuration
SMF_URL = ''
DATABASES['smf'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'alliance_smf',
    'USER': 'allianceserver-smf',
    'PASSWORD': 'password',
    'HOST': '127.0.0.1',
    'PORT': '3306',
}
#### ADD YOUR OWN LOCAL DATABASE DETAILS HERE
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'aauth',
    'USER': 'aauth',
    'PASSWORD': 'PASSWORD',
    'HOST': '127.0.0.1',
    'PORT': '3306',
}


ESI_SSO_CLIENT_ID = ''
ESI_SSO_CLIENT_SECRET = ''
ESI_SSO_CALLBACK_URL = ''


REGISTRATION_VERIFY_EMAIL = False
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''
#######################################
# Add any custom settings below here. #
#######################################

ROOT_URLCONF = 'myauth.urls'
WSGI_APPLICATION = 'myauth.wsgi.application'
STATIC_ROOT = "/var/www/myauth/static/"
BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "redis:6379",
        "OPTIONS": {
            "DB": 1,
        }
    }
}
