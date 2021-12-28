from django.shortcuts import redirect, render
from .forms import Formulario_contacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = Formulario_contacto()
    if request.method == 'POST':
        formulario_contacto=Formulario_contacto(data=request.POST) # cargo en el form la info que el ususario introdujo
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage(f"Mensaje desde App Django, El usuario {nombre} con direccion de correo electronica {email} escribe lo siguiente:\n {contenido}",
            "", ["prueba@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect('/contacto/?exito')
            except:
                return redirect('/contacto/?sinexito')

    return render(request, 'contacto/contacto.html', {'mi_formulario':formulario_contacto})