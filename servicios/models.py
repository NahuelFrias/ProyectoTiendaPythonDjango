from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # debo instalar Pilow
    imagen = models.ImageField(upload_to='servicios') #crea una carpeta dentro de media y guarda las imagenes
    created = models.DateTimeField(auto_now_add = True) # crea la fecha automaticamente
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo