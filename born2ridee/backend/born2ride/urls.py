"""
URL configuration for born2ride project.
"""
from django.contrib import admin
from django.urls import path, include

from django.http import JsonResponse

def root_view(request):
    return JsonResponse({
        "status": "Born 2 Ride Backend is Running!",
        "api_root": "/api/",
        "admin_panel": "/admin/"
    })

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('core_api.urls')),
]
