from django import forms
from .models import Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields= (
            'nombres',
            'apellidos',
            'trabajo',
            'departamento',
            'hv',
            'avatar',
            'habilidades',
        )
        labels = {
            'nombres': 'Nombre',
            'apellidos': 'Apellido',
            'trabajo': 'Trabajo',
            'departamento': 'Departamento',
            'hv': 'Hoja de Vida',
            'habilidades': 'Habilidades',
        }

        widgets = {
            'departamento': forms.Select(
                attrs={
                    'class': 'ContainerEmpleadoFormSelect form-select form-select-lg mb-3'}
            ),
            'habilidades': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'ContainerEmpleadoFormSelect'}
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'ContainerEmpleadoFormName',
                    'placeholder': 'Nombres'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'ContainerEmpleadoFormName',
                    'placeholder': 'Apellidos'
                }
            ),
            'trabajo': forms.Select(
                attrs={
                    'class': 'ContainerEmpleadoFormName form-select form-select-lg mb-3',
                    'placeholder': 'Trabajo'
                    }
            ),
        }