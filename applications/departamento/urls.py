from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'departamento_app'
urlpatterns = [
    path('ListaDepartamentos/', views.ListaDepartamentos.as_view(), name='ListaDepartamentos'),
    path('NuevoDepartamento/', views.NuevoDepartamento.as_view(), name='NuevoDepartamento'),
    path('ActualizarDepartamento/<pk>', views.ActualizarDepartamento.as_view(), name='ActualizarDepartamento'),
    path('EliminarDepartamento/<pk>', views.EliminarDepartamento.as_view(), name='EliminarDepartamento')
]