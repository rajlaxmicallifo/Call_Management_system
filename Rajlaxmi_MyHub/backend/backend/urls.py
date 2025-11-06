from django.http import JsonResponse 
from django.urls import path 
 
def health_check(request): 
    return JsonResponse({ 
        "status": "healthy", 
        "service": "Django API", 
        "message": "API is working on Vercel!" 
    }) 
 
def test_endpoint(request): 
    return JsonResponse({"message": "Test endpoint working!"}) 
 
urlpatterns = [ 
    path('', health_check), 
    path('health/', health_check), 
    path('test/', test_endpoint), 
] 
