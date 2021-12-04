from django.contrib import admin
from django.urls import path, include
from core import settings
from django.conf.urls.static import static
from core.views import home_page, support


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('support', support, name='support'),
    path('', include('app_account.urls')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
