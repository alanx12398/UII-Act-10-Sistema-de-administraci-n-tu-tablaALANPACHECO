from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_asistencia, name='agregar_asistencia'),
    path('editar/<int:id_asistencia>/', views.editar_asistencia, name='editar_asistencia'),
    path('eliminar/<int:id_asistencia>/', views.eliminar_asistencia, name='eliminar_asistencia'),
]