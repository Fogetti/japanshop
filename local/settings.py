from config.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'japanshop',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'japanshop',
        'PASSWORD': 'japanshop',
    }
}
