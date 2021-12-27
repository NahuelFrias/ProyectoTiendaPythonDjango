from django.shortcuts import redirect, render
from .forms import Formulario_contacto

# Create your views here.

def contacto(request):
    formulario_contacto = Formulario_contacto()
    if request.method == 'POST':
        formulario_contacto=Formulario_contacto(data=request.POST) # cargo en el form la info que el ususario introdujo
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            return redirect('/contacto/?exito')

    return render(request, 'contacto/contacto.html', {'mi_formulario':formulario_contacto})