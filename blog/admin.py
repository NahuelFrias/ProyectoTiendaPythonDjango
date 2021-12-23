from django.contrib import admin
from .models import Categoria, Post
# aca registro para que aparezca en admin
# Register your models here.

class Categoria_admin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class Post_admin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Categoria, Categoria_admin)
admin.site.register(Post, Post_admin)