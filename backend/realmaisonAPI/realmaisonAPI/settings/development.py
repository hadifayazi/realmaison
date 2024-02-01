from .base import *
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")


# email configurations
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
DOMAIN = os.environ.get('DOMAIN')
SITE_NAME = 'realmaison'


# db connection²
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE'),
        'NAME':  os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER_NAME'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'PORT': os.environ.get('PORT'),
        'HOST': os.environ.get('HOST')
    }
}
