from django.shortcuts import redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request) # creo el carro
    producto = Producto.objects.get(id=producto_id) # obtengo el producto
    carro.agregar(producto=producto) # agrego el producto al carro
    return redirect("Tienda") # redirecciono al url de la tienda

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")