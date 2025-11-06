from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Suscripcion

def inicio_crunchyroll(request):
    return render(request, 'inicio.html')

def agregar_Suscripcion(request):
    if request.method == 'POST':
        Suscripcion.objects.create(
            nombre_plan=request.POST['nombre_plan'],
            precio=request.POST['precio'],
            calidad_video=request.POST['calidad_video'],
            num_dispositivos=request.POST['num_dispositivos'],
            beneficio_extra=request.POST['beneficio_extra'],
            descarga_offline='descarga_offline' in request.POST
        )
        return redirect('ver_Suscripciones')
    return render(request, 'suscripciones/agregar_Suscripciones.html')

def ver_Suscripciones(request):
    suscripciones = Suscripcion.objects.all()
    return render(request, 'suscripciones/ver_Suscripciones.html', {'suscripciones': suscripciones})

def actualizar_Suscripcion(request, id):
    suscripcion = get_object_or_404(Suscripcion, id=id)
    if request.method == 'POST':
        suscripcion.nombre_plan = request.POST['nombre_plan']
        suscripcion.precio = request.POST['precio']
        suscripcion.calidad_video = request.POST['calidad_video']
        suscripcion.num_dispositivos = request.POST['num_dispositivos']
        suscripcion.beneficio_extra = request.POST['beneficio_extra']
        suscripcion.descarga_offline = 'descarga_offline' in request.POST
        suscripcion.save()
        return redirect('ver_Suscripciones')
    return render(request, 'suscripciones/actualizar_Suscripciones.html', {'suscripcion': suscripcion})

def borrar_Suscripcion(request, id):
    suscripcion = get_object_or_404(Suscripcion, id=id)
    
    if request.method == 'POST':
        # Confirmación para eliminar
        suscripcion.delete()
        return redirect('ver_Suscripciones')
    
    # Mostrar página de confirmación
    return render(request, 'suscripciones/borrar_Suscripcion.html', {'suscripcion': suscripcion})