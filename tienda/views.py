from django.shortcuts import render
from .models import Producto

# Create your views here.

def tienda(request):

    productos = Producto.objects.all() # almaceno todos los productos en la variable

    return render(request, 'tienda/tienda.html', {"productos":productos})