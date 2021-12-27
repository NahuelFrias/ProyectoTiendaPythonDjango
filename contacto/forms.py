from django import forms

class Formulario_contacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=30)
    email = forms.EmailField(label='Email', required=True, max_length=50)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)