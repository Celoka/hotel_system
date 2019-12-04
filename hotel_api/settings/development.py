
import os
from dotenv import load_dotenv
from .base import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'HOST': '127.0.0.1',
            'PORT': '5432',
    }
}
