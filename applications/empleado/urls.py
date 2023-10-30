from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'empleado_app'
urlpatterns = [
    path('CrearEmpleado/', views.CrearEmpleado.as_view(), name='CrearEmpleado'),
    path('ListarTodosLosEmpleados/', views.ListarTodosLosEmpleados.as_view(), name='ListarTodosLosEmpleados'),
    path('VerEmpleado/<pk>/', views.VerEmpleado.as_view(), name='VerEmpleado'),
    path('ActualizarEmpleado/<pk>', views.ActualizarEmpleado.as_view(), name='ActualizarEmpleado'),
    path('EliminarEmpleado/<pk>/', views.EliminarEmpleado.as_view(), name='EliminarEmpleado'),
]