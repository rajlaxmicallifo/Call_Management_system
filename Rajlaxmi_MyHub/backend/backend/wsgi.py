import os
import sys
import traceback

print("🚀 Starting Django WSGI application on Vercel...")

# Add project directories to Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
backend_dir = os.path.dirname(os.path.abspath(__file__))

if project_dir not in sys.path:
    sys.path.append(project_dir)
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

print(f"📁 Project directory: {project_dir}")
print(f"📁 Backend directory: {backend_dir}")
print(f"📁 Python path: {sys.path}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

try:
    print("🔄 Importing Django...")
    import django
    from django.conf import settings
    from django.core.wsgi import get_wsgi_application
    
    print("✅ Django imported successfully")
    print(f"🔧 DEBUG mode: {settings.DEBUG}")
    print(f"🌐 ALLOWED_HOSTS: {getattr(settings, 'ALLOWED_HOSTS', 'Not set')}")
    
    print("🔄 Setting up Django...")
    django.setup()
    
    print("🔄 Creating WSGI application...")
    application = get_wsgi_application()
    print("✅ Django WSGI application created successfully!")
    
except ImportError as e:
    print(f"❌ IMPORT ERROR: {e}")
    traceback.print_exc()
    
    def application(environ, start_response):
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [f"Import Error: {str(e)}".encode()]
        
except Exception as e:
    print(f"❌ SETUP ERROR: {e}")
    traceback.print_exc()
    
    def application(environ, start_response):
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [f"Setup Error: {str(e)}".encode()]