from django.contrib import admin
# importo servicio
from .models import Servicio
# Register your models here.

class Servicio_admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
# registro en el admin
admin.site.register(Servicio, Servicio_admin)