from django.contrib import admin
from django.urls import path, include  # Ensure to import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('transcript_api.urls')),  # Including app URLs
]
