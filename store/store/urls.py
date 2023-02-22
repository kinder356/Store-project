from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from products.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('products/', catalog, name='catalog'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)