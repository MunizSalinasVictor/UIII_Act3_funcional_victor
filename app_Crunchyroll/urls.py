from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_crunchyroll, name='inicio_crunchyroll'),
    path('suscripciones/agregar/', views.agregar_Suscripcion, name='agregar_Suscripcion'),
    path('suscripciones/ver/', views.ver_Suscripciones, name='ver_Suscripciones'),
    path('suscripciones/actualizar/<int:id>/', views.actualizar_Suscripcion, name='actualizar_Suscripcion'),
    path('suscripciones/borrar/<int:id>/', views.borrar_Suscripcion, name='borrar_Suscripcion'),
]