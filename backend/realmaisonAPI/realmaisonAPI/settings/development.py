from .base import *
SECRET_KEY = env("SECRET_KEY")
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME':  env('DB_NAME'),
        'USER': env('DB_USER_NAME'),
        'PASSWORD': env('DB_PASSWORD'),
        'PORT': env('PORT'),
        'HOST': env('HOST')
    }
}
