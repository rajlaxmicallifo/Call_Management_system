<<<<<<< HEAD
"""
WSGI config for backend project.
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
=======
import os
import sys
import traceback

print("🚀 STARTING DJANGO WSGI - ENHANCED DEBUGGING")

# Show current working directory and files
print(f"📁 Current working directory: {os.getcwd()}")
print("📂 Files in current directory:")
try:
    for item in os.listdir('.'):
        print(f"   - {item}")
except Exception as e:
    print(f"   ERROR listing directory: {e}")

# Add project directories to Python path
current_file = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(current_file))
backend_dir = os.path.dirname(current_file)

print(f"📁 Current file: {current_file}")
print(f"📁 Project directory: {project_dir}")
print(f"📁 Backend directory: {backend_dir}")

# Check if directories exist
print(f"📂 Project dir exists: {os.path.exists(project_dir)}")
print(f"📂 Backend dir exists: {os.path.exists(backend_dir)}")

# Add to Python path
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

print(f"📁 Python path: {sys.path}")

# Check if we can find critical files
critical_files = [
    'manage.py',
    'requirements.txt', 
    'backend/settings.py'
]

print("🔍 Checking for critical files:")
for file_path in critical_files:
    full_path = os.path.join(project_dir, file_path)
    exists = os.path.exists(full_path)
    print(f"   {file_path}: {'✅ EXISTS' if exists else '❌ MISSING'}")
>>>>>>> 8fdd39be4ccc5087c0af57a393f2fb4e858ef6c3

# Add project to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

print("🚀 Starting Django WSGI application...")
print(f"📁 Current directory: {current_dir}")
print(f"📁 Project directory: {project_dir}")
print(f"📁 Python path: {sys.path}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

<<<<<<< HEAD
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
=======
try:
    print("🔄 Attempting to import Django...")
    import django
    print("✅ Django imported successfully")
    
    print("🔄 Importing settings...")
    from django.conf import settings
    print("✅ Settings imported")
    
    print("🔄 Setting up Django...")
    django.setup()
    print("✅ Django setup completed")
    
    print("🔄 Creating WSGI application...")
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("🎉 SUCCESS: Django WSGI application loaded!")
    
except Exception as e:
    print(f"❌ CRITICAL ERROR: {e}")
    print("📋 Full traceback:")
    traceback.print_exc()
    
    def application(environ, start_response):
        response = f"""
        DJANGO SETUP FAILED!
        
        Error: {str(e)}
        
        Python Path: {sys.path}
        Current Directory: {os.getcwd()}
        Project Directory: {project_dir}
        Backend Directory: {backend_dir}
        
        Traceback:
        {traceback.format_exc()}
        """
        status = '500 Internal Server Error'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return [response.encode()]
>>>>>>> 8fdd39be4ccc5087c0af57a393f2fb4e858ef6c3
