from pathlib import Path
import os
import sys
from dotenv import load_dotenv

<<<<<<< HEAD
# Add this for Vercel path resolution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables
load_dotenv()

print("🚀 Django settings loading...")
print(f"📁 BASE_DIR: {Path(__file__).resolve().parent.parent}")
print(f"🔑 DEBUG: {os.environ.get('DEBUG', 'False') == 'True'}")
print(f"🌐 ALLOWED_HOSTS: {['.vercel.app', '.now.sh', '127.0.0.1', 'localhost', '192.168.1.17']}")

# ===============================================================
# BASE DIR
# ===============================================================
BASE_DIR = Path(__file__).resolve().parent.parent
=======
print("🚀 Django settings loading...")

try:
    # ===============================================================
    # VERCEL PATH FIXES - CRITICAL FOR DEPLOYMENT
    # ===============================================================
    BASE_DIR = Path(__file__).resolve().parent.parent
>>>>>>> 8fdd39be4ccc5087c0af57a393f2fb4e858ef6c3

    # Add project directories to Python path for Vercel
    project_root = BASE_DIR.parent  # Rajlaxmi_MyHub/backend
    if str(project_root) not in sys.path:
        sys.path.append(str(project_root))
    if str(BASE_DIR) not in sys.path:
        sys.path.append(str(BASE_DIR))

    print(f"📁 BASE_DIR: {BASE_DIR}")
    print(f"📁 Project Root: {project_root}")
    print(f"📁 Python Path: {sys.path}")

<<<<<<< HEAD
# Check if we're running on Vercel
IS_VERCEL = "VERCEL" in os.environ

# ✅ Vercel deployment hosts + local development
ALLOWED_HOSTS = [
    '.vercel.app',
    '.now.sh',
    '127.0.0.1', 
    'localhost',
    '192.168.1.17'
]

# ===============================================================
# APPLICATIONS (Django Admin Removed)
# ===============================================================
INSTALLED_APPS = [
    # Django core apps (Admin removed)
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
=======
    # Load environment variables
    load_dotenv()

    # ===============================================================
    # SECURITY SETTINGS
    # ===============================================================
    SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-s&fzh4!h@a_oy+toc2w#)3$+6ywgjp$#l0%65-d82x1e(8za4)')
>>>>>>> 8fdd39be4ccc5087c0af57a393f2fb4e858ef6c3

    # DEBUG = True for development, False for production
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'

    # Check if we're running on Vercel
    IS_VERCEL = "VERCEL" in os.environ or "VERCEL_ENV" in os.environ

<<<<<<< HEAD
# ===============================================================
# MIDDLEWARE (Admin middleware removed)
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
=======
    if IS_VERCEL:
        print("🌐 Running on Vercel production environment")
    else:
        print("💻 Running on local development environment")
>>>>>>> 8fdd39be4ccc5087c0af57a393f2fb4e858ef6c3

    # ✅ Vercel deployment hosts + local development
    ALLOWED_HOSTS = [
        '.vercel.app',
        '.now.sh',
        '.on.vercel.app',
        '127.0.0.1', 
        'localhost',
        '192.168.1.17',
        '0.0.0.0'
    ]

<<<<<<< HEAD
# Remove templates since we don't need admin templates
TEMPLATES = []
=======
    # ===============================================================
    # APPLICATIONS (Django Admin Removed)
    # ===============================================================
    INSTALLED_APPS = [
        # Django core apps
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third-party apps
        'rest_framework',
        'rest_framework.authtoken',  # ✅ Token authentication
        'corsheaders',
        'whitenoise',  # ✅ For Vercel static files

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

    # Template configuration
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
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
>>>>>>> 8fdd39be4ccc5087c0af57a393f2fb4e858ef6c3

    WSGI_APPLICATION = 'backend.wsgi.application'

<<<<<<< HEAD
# ===============================================================
# DATABASE (Vercel PostgreSQL + Local SQLite)
# ===============================================================
if IS_VERCEL or os.environ.get('DATABASE_URL'):
    # Production - Vercel PostgreSQL
    print("🔧 Using PostgreSQL database configuration...")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('PGDATABASE', 'neondb'),
            'USER': os.environ.get('PGUSER', 'neondb_owner'),
            'PASSWORD': os.environ.get('PGPASSWORD', 'npg_A5ZJiuz4DUXG'),
            'HOST': os.environ.get('PGHOST', 'ep-patient-credit-adlzkz3n-pooler.c-2.us-east-1.aws.neon.tech'),
            'PORT': '5432',
            'OPTIONS': {
                'sslmode': 'require',
            }
        }
    }
    print(f"✅ Database configured: {DATABASES['default']['HOST']}")
else:
    # Development - SQLite
    print("🔧 Using SQLite database configuration...")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
=======
    # ===============================================================
    # DATABASE (Vercel PostgreSQL + Local SQLite)
    # ===============================================================
    # Check for PostgreSQL environment variables first
    has_postgres_env = all([
        os.environ.get('PGHOST'),
        os.environ.get('PGDATABASE'), 
        os.environ.get('PGUSER'),
        os.environ.get('PGPASSWORD')
    ])

    if IS_VERCEL or has_postgres_env:
        # Production - Vercel PostgreSQL
        print("🔧 Using PostgreSQL database configuration...")
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.environ.get('PGDATABASE', 'neondb'),
                'USER': os.environ.get('PGUSER', 'neondb_owner'),
                'PASSWORD': os.environ.get('PGPASSWORD', 'npg_A5ZJiuz4DUXG'),
                'HOST': os.environ.get('PGHOST', 'ep-patient-credit-adlzkz3n-pooler.c-2.us-east-1.aws.neon.tech'),
                'PORT': os.environ.get('PGPORT', '5432'),
                'OPTIONS': {
                    'sslmode': 'require',
                },
                'CONN_MAX_AGE': 600,  # Better for serverless
            }
        }
        print(f"✅ Database configured for: {DATABASES['default']['HOST']}")
    else:
        # Development - SQLite
        print("🔧 Using SQLite database configuration...")
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
    # STATIC FILES (Vercel Optimized)
    # ===============================================================
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # WhiteNoise configuration for Vercel
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # Additional locations of static files
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

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
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://*.vercel.app",
        "https://*.on.vercel.app",
    ]

    # ===============================================================
    # BITRIX24 CONFIGURATION (Environment Variables)
    # ===============================================================
    BITRIX24_WEBHOOK_URL = os.environ.get('BITRIX24_WEBHOOK_URL', 'https://world.bitrix24.com/rest/244/8w0b44xg96oamfqt/')
    BITRIX24_DOMAIN = os.environ.get('BITRIX24_DOMAIN', 'world.bitrix24.com')

    BITRIX24_WEBHOOKS = {
        'lead_creation': BITRIX24_WEBHOOK_URL,
    }

    # ===============================================================
    # REST FRAMEWORK SETTINGS
    # ===============================================================
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',  # Changed for easier testing
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ],
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
        ],
        'DEFAULT_PARSER_CLASSES': [
            'rest_framework.parsers.JSONParser',
        ],
    }

    # ===============================================================
    # CSRF & SECURITY SETTINGS
    # ===============================================================
    CSRF_TRUSTED_ORIGINS = [
        'https://*.vercel.app',
        'https://*.now.sh',
        'https://*.on.vercel.app',
        'http://192.168.1.17:8000',
        'http://localhost:8000',
        'http://127.0.0.1:8000',
        'http://localhost:3000',
    ]

    # Security settings for production
    if not DEBUG:
        SECURE_SSL_REDIRECT = True
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
        SECURE_BROWSER_XSS_FILTER = True
        SECURE_CONTENT_TYPE_NOSNIFF = True
        SECURE_HSTS_SECONDS = 31536000  # 1 year
        SECURE_HSTS_INCLUDE_SUBDOMAINS = True
        SECURE_HSTS_PRELOAD = True

    # ===============================================================
    # LOGGING (Enhanced for Vercel)
    # ===============================================================
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'stream': sys.stdout,
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'WARNING',  # Reduce database query logs
                'propagate': False,
            },
>>>>>>> 8fdd39be4ccc5087c0af57a393f2fb4e858ef6c3
        }
    }

    # ===============================================================
    # VERCEL-SPECIFIC SETTINGS
    # ===============================================================
    if IS_VERCEL:
        # WhiteNoise configuration for Vercel
        WHITENOISE_USE_FINDERS = True
        WHITENOISE_MANIFEST_STRICT = False
        WHITENOISE_ALLOW_ALL_ORIGINS = True
        WHITENOISE_AUTOREFRESH = True
        
        # Serverless-specific settings
        DATABASES['default']['CONN_MAX_AGE'] = 60  # Lower for serverless

    # ===============================================================
    # APPLICATION SPECIFIC SETTINGS
    # ===============================================================
    # Add any custom settings here

<<<<<<< HEAD
# ===============================================================
# STATIC FILES (Simplified for Vercel)
# ===============================================================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

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
    "https://call-management-backend-26upd5vex.vercel.app",  # Your current Vercel app
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

print("✅ Django settings loaded successfully!")
print("🎯 Django admin removed - Using API-only mode")
=======
    print("✅ Django settings loaded successfully!")
    print(f"🔧 Debug mode: {DEBUG}")
    print(f"🌐 Allowed hosts: {ALLOWED_HOSTS}")
    print(f"📁 Static root: {STATIC_ROOT}")
    print(f"🗄️ Database: {DATABASES['default']['ENGINE']}")
    print("🎯 Django API-only mode - Ready for Vercel deployment!")

except Exception as e:
    print(f"❌ ERROR loading Django settings: {e}")
    import traceback
    traceback.print_exc()
    raise
>>>>>>> 8fdd39be4ccc5087c0af57a393f2fb4e858ef6c3
