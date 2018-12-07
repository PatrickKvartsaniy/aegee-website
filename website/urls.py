from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('website.apps.landing.urls')),
    path('blog/', include('website.apps.blog.urls')),
    path('about/', include('website.apps.about.urls')),
    path('events/', include('website.apps.events.urls')),
     path('projects/', include('website.apps.projects.urls')),
    path('contact/', include('website.apps.contact.urls')),
    path('api', include('website.apps.api.urls')),
    # path('^api-auth/', include('rest_framework.urls'))
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
