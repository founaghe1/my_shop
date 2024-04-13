
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static 

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myShop/', include("produits.urls")),
]

# Serve les fichiers média en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()