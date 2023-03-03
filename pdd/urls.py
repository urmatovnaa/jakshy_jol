from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pdd import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('apps.about_us.urls')),
    path('test/', include('apps.test_pdd.urls')),
    path('home/', include('apps.home_page.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
