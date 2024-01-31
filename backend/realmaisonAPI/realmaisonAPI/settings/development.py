from .base import *
import os
from dotenv import load_dotenv

load_dotenv()
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
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
