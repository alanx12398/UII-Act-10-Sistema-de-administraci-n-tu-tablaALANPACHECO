from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_inscripcion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=[
        ('presente', 'Presente'),
        ('ausente', 'Ausente'),
        ('tardanza', 'Tardanza')
    ])
    clase = models.CharField(max_length=50)
    entrada = models.TimeField()
    salida = models.TimeField()
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Asistencia {self.id_alumno.nombre} - {self.fecha}'