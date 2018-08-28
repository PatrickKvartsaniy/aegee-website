from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('landing.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('events/', include('events.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
