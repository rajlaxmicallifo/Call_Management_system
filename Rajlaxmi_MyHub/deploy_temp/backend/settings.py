from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===============================================================
# BASE DIR
# ===============================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================================================
# SECURITY SETTINGS
# ===============================================================
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-s&fzh4!h@a_oy+toc2w#)3$+6ywgjp$#l0%65-d82x1e(8za4)')

# DEBUG = True for development, False for production
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ✅ Vercel deployment hosts + local development
ALLOWED_HOSTS = [
    '.vercel.app',
    '.now.sh',
    '127.0.0.1', 
    'localhost',
    '192.168.1.17'
]

# ===============================================================
# APPLICATIONS
# ===============================================================
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',  # ✅ Token authentication
    'corsheaders',
    'whitenoise.runserver_nostatic',  # ✅ For Vercel static files

    # Your apps
    'accounts',  # For user auth
    'calls',     # For call data & recordings
]

# ===============================================================
# MIDDLEWARE
# ===============================================================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be first
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ For Vercel
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===============================================================
# URL CONFIG
# ===============================================================
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# ===============================================================
# DATABASE (Vercel PostgreSQL + Local SQLite)
# ===============================================================
if os.environ.get('DATABASE_URL'):
    # Production - Vercel PostgreSQL
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=not DEBUG
        )
    }
else:
    # Development - SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ===============================================================
# PASSWORD VALIDATORS
# ===============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===============================================================
# INTERNATIONALIZATION
# ===============================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ===============================================================
# STATIC FILES (Vercel Configuration)
# ===============================================================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ===============================================================
# MEDIA FILES (call recordings, uploads)
# ===============================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ===============================================================
# DEFAULT PRIMARY KEY
# ===============================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===============================================================
# CORS SETTINGS (allow Flutter mobile app + Vercel)
# ===============================================================
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'accept',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://192.168.1.17:8000",
    "https://your-app.vercel.app",  # Your Flutter web app
]

# ===============================================================
# BITRIX24 CONFIGURATION (Environment Variables)
# ===============================================================
BITRIX24_WEBHOOK_URL = os.environ.get('BITRIX24_WEBHOOK_URL', 'https://world.bitrix24.com/rest/244/8w0b44xg96oamfqt/')
BITRIX24_DOMAIN = os.environ.get('BITRIX24_DOMAIN', 'world.bitrix24.com')

BITRIX24_WEBHOOKS = {
    'lead_creation': os.environ.get('BITRIX24_WEBHOOK_URL', 'https://world.bitrix24.com/rest/244/8w0b44xg96oamfqt/'),
}

# ===============================================================
# REST FRAMEWORK SETTINGS
# ===============================================================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

# ===============================================================
# CSRF & SECURITY SETTINGS
# ===============================================================
CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'http://192.168.1.17:8000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

# ===============================================================
# LOGGING
# ===============================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    }
}