import os 
import sys 
import traceback 
 
print("?? Starting Django WSGI application on Vercel...") 
 
# Add project directories to Python path 
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
if project_dir not in sys.path: 
    sys.path.append(project_dir) 
 
print(f"?? Project directory: {project_dir}") 
print(f"?? Python path: {sys.path}") 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings') 
 
try: 
    from django.core.wsgi import get_wsgi_application 
    application = get_wsgi_application() 
    print("? Django WSGI application loaded successfully!") 
except Exception as e: 
    print(f"? Django setup failed: {e}") 
    traceback.print_exc() 
 
    def application(environ, start_response): 
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')]) 
        return [f"Django Error: {str^(e^)}".encode()] 
