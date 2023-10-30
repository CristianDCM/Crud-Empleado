from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView , DetailView
from .models import Empleado 
from .forms import EmpleadoForm

class CrearEmpleado(CreateView):
    model = Empleado
    template_name = 'empleado/CrearEmpleado.html'
    context_object_name = 'CrearEmpleado'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:ListarTodosLosEmpleados')

    def form_valid(self, form):
        empleado = form.save(commit=False) 
        empleado.save()
        return super(CrearEmpleado, self).form_valid(form)
    
class ListarTodosLosEmpleados(ListView):
    template_name = 'empleado/ListarTodosLosEmpleados.html'
    paginate_by = 4
    ordering = 'apellidos'
    context_object_name = 'listaEmpleados'
    model = Empleado  

    def get_queryset(self):
        palabraClave = self.request.GET.get('kword', '')
        listaEmpleados = Empleado.objects.filter(
            apellidos__icontains=palabraClave
        )
        print('listaEmpleados: ', listaEmpleados)
        return listaEmpleados
    
class VerEmpleado(DetailView):
    model = Empleado
    template_name = 'empleado/VerEmpleado.html'
    context_object_name = 'VerEmpleado'

    def get_context_data(self, **kwargs):
        context = super(VerEmpleado, self).get_context_data(**kwargs)
        context['habilidades'] = self.object.habilidades.all()
        context['titulo'] = 'Empleado del mes'
        return context
    success_url = reverse_lazy('empleado_app:ListarTodosLosEmpleados')

class ActualizarEmpleado(UpdateView):
    template_name = 'empleado/ActualizarEmpleado.html'
    context_object_name = 'ActualizarEmpleado'
    model = Empleado
    fields = ['nombres', 'apellidos', 'trabajo', 'departamento', 'hv', 'habilidades', 'avatar']

    success_url = reverse_lazy('empleado_app:ListarTodosLosEmpleados')

class EliminarEmpleado(DeleteView):
    model = Empleado
    context_object_name = 'EliminarEmpleado'
    template_name = 'empleado/EliminarEmpleado.html'

    success_url = reverse_lazy('empleado_app:ListarTodosLosEmpleados')