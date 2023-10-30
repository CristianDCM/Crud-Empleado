from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento
from .forms import NuevoDepartamentoForm

class NuevoDepartamento(CreateView):
    model = Departamento
    template_name = 'departamento/NuevoDepartamento.html'
    context_object_name = 'NuevoDepartamento'
    form_class = NuevoDepartamentoForm
    success_url = reverse_lazy('departamento_app:ListaDepartamentos')

    def form_valid(self, form):
        departament = form.save(commit=False)
        departament.save()
        return super(NuevoDepartamento, self).form_valid(form)

class ListaDepartamentos(ListView):
    model = Departamento
    template_name = 'departamento/ListaDepartamentos.html'
    context_object_name = 'departamentos'

    def get_queryset(self):
        palabraClave = self.request.GET.get('kword', '')
        listaDepartamentos = Departamento.objects.filter(
            nombreDepartamento__icontains=palabraClave
        )
        print('listaDepartamentos: ', listaDepartamentos)
        return listaDepartamentos

class ActualizarDepartamento(UpdateView):
    model = Departamento
    template_name = 'departamento/ActualizarDepartamento.html'
    context_object_name = 'ActualizarDepartamento'
    fields = ['nombreDepartamento', 'siglaDepartamento', 'activoDepartamento']
    success_url = reverse_lazy('departamento_app:ListaDepartamentos')
 
class EliminarDepartamento(DeleteView):
    model = Departamento
    template_name = 'departamento/EliminarDepartamento.html'
    context_object_name = 'EliminarDepartamento'
    success_url = reverse_lazy('departamento_app:ListaDepartamentos')