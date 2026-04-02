# LittleLemon/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # CHANGE CETTE LIGNE :
    path('admin/', admin.site.urls),  # <--- .urls et non .status_code
    
    path('api/', include('LittleLemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]