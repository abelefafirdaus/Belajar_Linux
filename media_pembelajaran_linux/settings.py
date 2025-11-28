from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# NOTE: ganti dengan secret key yang aman untuk production
SECRET_KEY = 'django-insecure-ganti_ini_dengan_key_baru_kamu'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # default django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local apps
    'pembelajaran',
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

ROOT_URLCONF = 'media_pembelajaran_linux.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Kita biarkan kosong sehingga APP_DIRS=True akan mencari templates di setiap app
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

WSGI_APPLICATION = 'media_pembelajaran_linux.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ... (kode atas biarkan sama) ...

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- TAMBAHAN KONFIGURASI LOGIN ---
LOGIN_URL = 'pembelajaran:login'
LOGIN_REDIRECT_URL = 'pembelajaran:index'
LOGOUT_REDIRECT_URL = 'pembelajaran:login'

# settings.py paling bawah

# Ini memberitahu Django: "Kalau ada user nyasar ke halaman terkunci, lempar ke sini"
LOGIN_URL = 'pembelajaran:login' 

# Ini memberitahu Django: "Kalau habis login tapi tidak ada tujuan khusus, lempar ke sini"
LOGIN_REDIRECT_URL = 'pembelajaran:index'

# Ini memberitahu Django: "Kalau logout, lempar ke sini"
LOGOUT_REDIRECT_URL = 'pembelajaran:login'