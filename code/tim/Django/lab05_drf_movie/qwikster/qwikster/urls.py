"""******** PROJECT ******** URL Configuration"""

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
    # path('', include('movies.urls')),
