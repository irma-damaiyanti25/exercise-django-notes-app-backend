from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-!&r-$6sx94gtbk8*cvy1s6cbb6%g6pjno#$7@(6^iyji#w&a+&'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

