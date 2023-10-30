from django.db import models

class Departamento(models.Model):
    nombreDepartamento= models.CharField('nombreDepartamento', max_length=50)
    siglaDepartamento= models.CharField('siglaDepartamento', max_length=2, unique=True)
    activoDepartamento= models.BooleanField('active', default=False)
    search_fields = ('nombreDepartamento', 'siglaDepartamento',)
    list_filter = ('nombreDepartamento',)
    
    class Meta:
        verbose_name = 'nombreDepartamento'
        verbose_name_plural = 'nombreDepartamento'
        ordering = ['nombreDepartamento']
        unique_together = ('nombreDepartamento', 'siglaDepartamento')

    def __str__(self):
        return self.nombreDepartamento + '-' + self.siglaDepartamento + '-' + str(self.id)