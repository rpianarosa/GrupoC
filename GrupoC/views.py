
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from GrupoC.models import Cerveza, Cerveceria, Experiencia

def PreInicio(req):

    return render(req,'GrupoC/preinicio.html')

def Inicio(req):

    return render(req,'GrupoC/inicio.html')

def Contacto(req):

    return render(req,'GrupoC/contacto.html')

class CervezaList (ListView):
    model= Cerveza
    template_name = "GrupoC/cerveza_list.html"

class CervezaDetail (DetailView):
    model= Cerveza
    template_name = "GrupoC/cerveza_detail.html"

class CervezaUpdate (UpdateView):
    model= Cerveza
    success_url = '/Cerveblog/listaCervezas'
    fields= ['nombre' , 'IBU', 'grad_alcohol']
    template_name = "GrupoC/cerveza_form.html"

class CervezaDelete (DeleteView):
    model= Cerveza
    success_url = '/Cerveblog/listaCervezas'
    template_name = "GrupoC/cerveza_conf_delete.html"

class CervezaCreate (CreateView):
    model= Cerveza
    success_url = '/Cerveblog/listaCervezas'
    fields= ['nombre' , 'IBU', 'grad_alcohol']
    template_name = "GrupoC/cerveza_form.html"




class CerveceriaList (ListView):
    model= Cerveceria
    template_name = "GrupoC/cerveceria_list.html"
class CerveceriaCreate (CreateView):
    model= Cerveceria
    success_url = '/Cerveblog/listaCervecerias'
    fields= ['nombre' , 'dire']
    template_name = "GrupoC/cerveceria_form.html"




class ExperienciaList (ListView):
    model= Experiencia
    template_name = "GrupoC/experiencia_list.html"

class ExperienciaDetail (DetailView):
    model= Experiencia
    template_name = "GrupoC/experiencia_detail.html"

class ExperienciaDelete (DeleteView):
    model= Experiencia
    success_url = '/Cerveblog/listaExperiencia'
    template_name = "GrupoC/experiencia_conf_delete.html"

class ExperienciaCreate (CreateView):
    model= Experiencia
    success_url = '/Cerveblog/listaExperiencia'
    fields= ['nombre' , 'apellido', 'cerv_tomada', 'cerv_atend', 'punt_cerveza', 'punt_cerveceria']
    template_name = "GrupoC/experiencia_form.html"
