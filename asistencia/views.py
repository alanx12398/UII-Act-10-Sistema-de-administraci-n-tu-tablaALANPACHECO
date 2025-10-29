from django.shortcuts import render, redirect, get_object_or_404
from .models import Asistencia, Alumno
from django.contrib import messages

def index(request):
    asistencias = Asistencia.objects.all().order_by('-fecha')
    return render(request, 'asistencia/index.html', {'asistencias': asistencias})

def agregar_asistencia(request):
    if request.method == 'POST':
        try:
            alumno = Alumno.objects.get(id_alumno=request.POST['id_alumno'])
            asistencia = Asistencia(
                fecha=request.POST['fecha'],
                estado=request.POST['estado'],
                clase=request.POST['clase'],
                entrada=request.POST['entrada'],
                salida=request.POST['salida'],
                id_alumno=alumno
            )
            asistencia.save()
            messages.success(request, 'Asistencia registrada!')
            return redirect('index')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    alumnos = Alumno.objects.all()
    return render(request, 'asistencia/agregar_asistencia.html', {'alumnos': alumnos})

def editar_asistencia(request, id_asistencia):
    asistencia = get_object_or_404(Asistencia, id_asistencia=id_asistencia)
    
    if request.method == 'POST':
        try:
            asistencia.fecha = request.POST['fecha']
            asistencia.estado = request.POST['estado']
            asistencia.clase = request.POST['clase']
            asistencia.entrada = request.POST['entrada']
            asistencia.salida = request.POST['salida']
            asistencia.save()
            messages.success(request, 'Asistencia actualizada!')
            return redirect('index')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'asistencia/editar_asistencia.html', {'asistencia': asistencia})

def eliminar_asistencia(request, id_asistencia):
    asistencia = get_object_or_404(Asistencia, id_asistencia=id_asistencia)
    
    if request.method == 'POST':
        asistencia.delete()
        messages.success(request, 'Asistencia eliminada!')
        return redirect('index')
    
    return render(request, 'asistencia/eliminar_asistencia.html', {'asistencia': asistencia})