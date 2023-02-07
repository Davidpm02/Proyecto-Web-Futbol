from .base import *   #Importamos todo del archivo base.py para que no nos salten errores.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": 'BBDD_Web_Futbol',
        "USER": 'postgres',
        "PASSWORD": 'Xispita18.',
        "HOST": 'localhost',
        "PORT": '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
     BASE_DIR / "static"
]