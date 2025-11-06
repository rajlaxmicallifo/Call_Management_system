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

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

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