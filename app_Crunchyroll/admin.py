from django.contrib import admin
from .models import Suscripcion, Contenido, Usuario

@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ['nombre_plan', 'precio', 'calidad_video', 'num_dispositivos']

@admin.register(Contenido)
class ContenidoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'fecha_lanzamiento']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre_usuario', 'email', 'fecha_registro']