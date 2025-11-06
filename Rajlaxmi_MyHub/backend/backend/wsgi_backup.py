"""
WSGI config for backend project.
"""

import os
import sys

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_dir not in sys.path:
    sys.path.append(project_dir)

print("🚀 Starting Django WSGI application...")
print(f"📁 Project directory: {project_dir}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("✅ Django WSGI application loaded successfully!")
    
except Exception as e:
    print(f"❌ Django setup failed: {e}")
    import traceback
    traceback.print_exc()
    
    # Fallback application
    def application(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [f"Django WSGI Error: {str(e)}".encode()]