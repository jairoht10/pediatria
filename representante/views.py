from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Representante
from .forms import RepresentanteForm
from base.models import Municipio, Parroquia

# Create your views here.

#class FrenteList(ListView):
#    model = Frente
#    template_name = "frente.lista.html"

#    def get_queryset(self):
#        queryset = Frente.objects.filter(user=self.request.user)
#        return queryset

class RepresentanteCreate(CreateView):
    model = Representante
    form_class = RepresentanteForm
    template_name = "representante.registro.template.html"
    success_url = reverse_lazy('representante_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.nombre = form.cleaned_data['nombre']
        self.object.apellido = form.cleaned_data['apellido']
        self.object.cedula = form.cleaned_data['cedula']
        self.object.telefono = form.cleaned_data['telefono']
        self.object.correo = form.cleaned_data['correo']
        self.object.parroquia = form.cleaned_data['parroquia']
        user = self.request.user
        self.object.user = user
        self.object.save()

        #Frente.objects.create(
        #    nombre = form.cleaned_data['frente_nombre'],
        #    persona = self.object,
        #    municipio = form.cleaned_data['municipio'],
        #    parroquia = form.cleaned_data['parroquia'],
        #    user = self.request.user
        #)

        return super(RepresentanteCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(RepresentanteCreate, self).form_invalid(form)


class RepresentanteList(ListView):
    model = Representante
    template_name = "representante.lista.template.html"

    def get_queryset(self):
        queryset = Representante.objects.filter(user=self.request.user)
        return queryset
