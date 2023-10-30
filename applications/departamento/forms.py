from django import forms
from .models import Departamento

class NuevoDepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = (
            'nombreDepartamento',
            'siglaDepartamento',
            'activoDepartamento',
        )
        labels = {
            'nombreDepartamento': 'Nombre Departamento',
            'siglaDepartamento': 'Sigla Departamento',
            'activoDepartamento': 'Activo',
        }
        widgets = {
            'activoDepartamento': forms.CheckboxInput(
                attrs={
                    'class': 'ContainerEmpleadoFormSelect',
                }
            ), 
            'nombreDepartamento':forms.TextInput(
                attrs={
                    'class': 'ContainerEmpleadoFormName',
                    'placeholder': 'Nombre Departamento',
                }
            ),
            'siglaDepartamento':forms.TextInput(
                attrs={
                    'class': 'ContainerEmpleadoFormName',
                    'placeholder': 'Sigla Departamento',
                }
            ),
        }
