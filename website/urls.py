from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from landing import views as landing_views
from contact import views as contact_views
from blog import views as blog_views
from about import views as about_views


urlpatterns = [
    path('', landing_views.index),
    path('contact/', contact_views.index),
    path('blog/', blog_views.index),
    path('about/', about_views.index),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
