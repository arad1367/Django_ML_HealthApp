from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthApp/', include('healthApp.urls')), # localhost:8000/healthApp/
    path('users/', include('users.urls')), # localhost:8000/users/
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)