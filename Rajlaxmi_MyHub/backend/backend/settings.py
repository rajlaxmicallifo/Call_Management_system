    from pathlib import Path
    import os
    import sys
    from dotenv import load_dotenv

    # ===============================================================
    # VERCEL PATH FIXES - CRITICAL FOR DEPLOYMENT
    # ===============================================================
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Add project directories to Python path for Vercel
    project_root = BASE_DIR.parent  # Rajlaxmi_MyHub/backend
    if str(project_root) not in sys.path:
        sys.path.append(str(project_root))
    if str(BASE_DIR) not in sys.path:
        sys.path.append(str(BASE_DIR))

    print("🚀 Django settings loading...")
    print(f"📁 BASE_DIR: {BASE_DIR}")
    print(f"📁 Project Root: {project_root}")

    # Load environment variables
    load_dotenv()

    # ===============================================================
    # SECURITY SETTINGS
    # ===============================================================
    SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-s&fzh4!h@a_oy+toc2w#)3$+6ywgjp$#l0%65-d82x1e(8za4)')

    # DEBUG = True for development, False for production
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'

    # Check if we're running on Vercel
    IS_VERCEL = "VERCEL" in os.environ

    if IS_VERCEL:
        print("🌐 Running on Vercel production environment")
    else:
        print("💻 Running on local development environment")

    # ✅ Vercel deployment hosts + local development
    ALLOWED_HOSTS = [
        '.vercel.app',
        '.now.sh',
        '127.0.0.1', 
        'localhost',
        '192.168.1.17',
        '0.0.0.0'
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

        # Third-party apps
        'rest_framework',
        'rest_framework.authtoken',  # ✅ Token authentication
        'corsheaders',
        'whitenoise',  # ✅ Simplified for Vercel

        # Your apps
        'accounts',  # For user auth
        'calls',     # For call data & recordings
    ]

    # ===============================================================
    # MIDDLEWARE (Admin middleware removed)
    # ===============================================================
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',  # Must be first
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ For Vercel - Moved up
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

    # Minimal template configuration (if needed for DRF)
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

    WSGI_APPLICATION = 'backend.wsgi.application'

    # ===============================================================
    # DATABASE (Vercel PostgreSQL + Local SQLite)
    # ===============================================================
    if IS_VERCEL:
        # Production - Vercel PostgreSQL
        print("🔧 Using PostgreSQL database configuration for Vercel...")
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
    elif os.environ.get('DATABASE_URL'):
        # Production with DATABASE_URL
        import dj_database_url
        print("🔧 Using DATABASE_URL configuration...")
        DATABASES = {
            'default': dj_database_url.config(
                default=os.environ.get('DATABASE_URL'),
                conn_max_age=600,
                ssl_require=True
            )
        }
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
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ],
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
        ],
    }

    # ===============================================================
    # CSRF & SECURITY SETTINGS
    # ===============================================================
    CSRF_TRUSTED_ORIGINS = [
        'https://*.vercel.app',
        'https://*.now.sh',
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
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'stream': sys.stdout,  # Important for Vercel
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO' if DEBUG else 'WARNING',
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
        }
    }

    # ===============================================================
    # VERCEL-SPECIFIC SETTINGS
    # ===============================================================
    if IS_VERCEL:
        # Ensure WhiteNoise works correctly
        WHITENOISE_USE_FINDERS = True
        WHITENOISE_MANIFEST_STRICT = False
        WHITENOISE_ALLOW_ALL_ORIGINS = True
        
        # Disable Django's built-in static file handling in production
        DISABLE_COLLECTSTATIC = os.environ.get('DISABLE_COLLECTSTATIC', '0') == '1'

    print("✅ Django settings loaded successfully!")
    print(f"🔧 Debug mode: {DEBUG}")
    print(f"🌐 Allowed hosts: {ALLOWED_HOSTS}")
    print(f"📁 Static root: {STATIC_ROOT}")
    print("🎯 Django admin removed - Using API-only mode")