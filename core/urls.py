from django.urls import path
from .views import home, acerca_de
from .views import contactos, vehiculo_1
from .views import home2, home3
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home,name="home"),
    path('home2/', home2,name="home2"),
    path('home3/', home3,name="home3"),
    path('acerca_de/', acerca_de, name="acerca"),
    path('contactos/', contactos,name="contactos"),
    path('vehiculo_1/', vehiculo_1,name="vehiculo_1"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)