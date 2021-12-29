from django.urls import path
from . import views

# para utilizar estas url de forma mas comoda
app_name="carro"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"), #producto_id esta declarado como una llave en carro.py
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]