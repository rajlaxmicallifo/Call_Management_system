"""
WSGI config for backend project.
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add project to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

print("🚀 Starting Django WSGI application...")
print(f"📁 Current directory: {current_dir}")
print(f"📁 Project directory: {project_dir}")
print(f"📁 Python path: {sys.path}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

print("✅ Environment variables set")

try:
    # Test imports
    print("🔧 Testing imports...")
    from django.conf import settings
    print("✅ Django settings imported")
    
    import accounts
    print("✅ Accounts app imported")
    
    import calls  
    print("✅ Calls app imported")
    
    # Load application
    application = get_wsgi_application()
    print("✅ Django WSGI application loaded successfully!")
    
except Exception as e:
    print(f"❌ Django setup failed: {e}")
    import traceback
    print("📋 Full traceback:")
    traceback.print_exc()
    
    # Create simple error app
    def error_app(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [f"Django Error: {str(e)}".encode()]
    
    application = error_app