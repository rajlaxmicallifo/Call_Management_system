import os
import sys
from http.server import BaseHTTPRequestHandler
import json

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("🚀 Starting minimal Django app...")
print(f"📁 Python path: {sys.path}")
print(f"📁 Current directory: {os.getcwd()}")
print(f"📁 Files in current directory: {os.listdir('.')}")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"📨 Received request: {self.path}")
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "status": "working", 
            "message": "Simple API test",
            "path": self.path,
            "django_loaded": False
        }
        
        # Try to load Django
        try:
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
            from django.conf import settings
            response["django_loaded"] = True
            response["debug_mode"] = settings.DEBUG
            print("✅ Django settings loaded successfully")
        except Exception as e:
            response["django_error"] = str(e)
            print(f"❌ Django settings failed: {e}")
        
        response_json = json.dumps(response)
        print(f"📤 Sending response: {response_json}")
        self.wfile.write(response_json.encode('utf-8'))

def app(environ, start_response):
    print(f"🚀 WSGI request: {environ.get('PATH_INFO', '/')}")
    
    # Simple WSGI application
    status = '200 OK'
    response_headers = [('Content-type', 'application/json')]
    start_response(status, response_headers)
    
    response = {
        "status": "working",
        "message": "WSGI app is running",
        "path": environ.get('PATH_INFO', '/'),
        "method": environ.get('REQUEST_METHOD', 'GET')
    }
    
    return [json.dumps(response).encode('utf-8')]

# For Vercel Python runtime
application = app