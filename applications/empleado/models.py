from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

JOB_CHOICES = (
    ('0', 'Contador'),
    ('1', 'Administrador'),
    ('2', 'Economista'),
    ('3', 'Ingeniero'),
    ('4', 'Desarrollador'),
)

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidades', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.habilidad + '-' + str(self.id)
        
class Empleado(models.Model):
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    trabajo = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    hv = RichTextField(default='None', blank=True)
    avatar = models.ImageField(upload_to='empleados', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return self.apellidos + ' ' + self.nombres + '-' + str(self.id)
         