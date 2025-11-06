from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.db import connection
from django.core.management import call_command

# ===============================================================
# HEALTH CHECK ENDPOINT
# ===============================================================
def health_check(request):
    return JsonResponse({
        "status": "healthy", 
        "service": "Django API",
        "debug": settings.DEBUG
    })

# ===============================================================
# MIGRATION ENDPOINT
# ===============================================================
def run_migrations(request):
    try:
        # Run migrations
        call_command('migrate', verbosity=0)
        
        # Check if tables were created
        with connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = [row[0] for row in cursor.fetchall()]
        
        return JsonResponse({
            "status": "success",
            "message": "Migrations completed successfully",
            "tables_created": tables
        })
    except Exception as e:
        return JsonResponse({
            "status": "error", 
            "message": str(e)
        }, status=500)

# ===============================================================
# CREATE SUPERUSER ENDPOINT
# ===============================================================
def create_superuser(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    try:
        # Check if user already exists
        if User.objects.filter(username='admin').exists():
            return JsonResponse({"status": "superuser already exists"})
        
        # Create superuser with proper method
        user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com', 
            password='admin123'
        )
        return JsonResponse({
            "status": "superuser created successfully",
            "username": "admin",
            "password": "admin123"
        })
    except Exception as e:
        return JsonResponse({
            "status": "error", 
            "message": str(e),
            "debug_info": "Check if auth_user table exists"
        }, status=500)

# ===============================================================
# CHECK DATABASE TABLES
# ===============================================================
def check_tables(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = [row[0] for row in cursor.fetchall()]
        
        return JsonResponse({
            "status": "success",
            "tables": tables,
            "has_auth_tables": 'auth_user' in tables
        })
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

# ===============================================================
# API ADMIN INTERFACE
# ===============================================================
def api_admin(request):
    return JsonResponse({
        "message": "API Admin Panel",
        "available_endpoints": {
            "health": "/health/",
            "migrations": "/migrate/",
            "create_superuser": "/create-superuser/",
            "check_tables": "/check-tables/",
            "user_auth": "/api/accounts/",
            "calls_api": "/api/calls/"
        },
        "status": "API is running successfully on Vercel"
    })

# ===============================================================
# CATCH-ALL ROUTE FOR DEBUGGING (MUST BE LAST)
# ===============================================================
def catch_all(request, path):
    return JsonResponse({
        "error": "Endpoint not found but Django is running!",
        "requested_path": f"/{path}",
        "available_endpoints": [
            "/", 
            "/health/", 
            "/admin/", 
            "/migrate/", 
            "/create-superuser/", 
            "/check-tables/", 
            "/api/accounts/",
            "/api/calls/"
        ],
        "debug_info": {
            "django_loaded": True,
            "debug_mode": settings.DEBUG
        }
    }, status=404)

# ===============================================================
# URL PATTERNS (CORRECT ORDER)
# ===============================================================
urlpatterns = [
    # Basic endpoints
    path('', health_check),
    path('health/', health_check),
    path('migrate/', run_migrations),
    path('create-superuser/', create_superuser),
    path('check-tables/', check_tables),
    path('admin/', api_admin),
    
    # ✅ API ROUTES - MUST COME BEFORE CATCH-ALL
    path('api/', include('accounts.urls')),  # User authentication
    path('api/', include('calls.urls')),     # Call management
    
    # ✅ CATCH-ALL ROUTE - MUST BE LAST
    path('<path:path>', catch_all),
]

# Remove Django admin from installed apps in settings.py too