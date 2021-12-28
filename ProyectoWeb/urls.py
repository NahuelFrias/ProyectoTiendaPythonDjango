from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # incluyo las url de mi app
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/', include('tienda.urls')),
    path('', include('ProyectoWebApp.urls')),
]
