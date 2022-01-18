
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

def Cervezas(req):

    return render(req,'GrupoC/cervezas.html')

    
def Cervecerias(req):

    return render(req,'GrupoC/cervecerias.html')

def Experiencias(req):

    return render(req,'GrupoC/experiencias.html')


class CervezaList (ListView):
    model= Cerveza
    template_name = "GrupoC/cerveza_list.html"

class CervezaDetail (DetailView):
    model= Cerveza
    template_name = "GrupoC/cerveza_detail.html"

class CervezaUpdate (UpdateView):
    model= Cerveza
    success_url = '/GrupoC/listaCervezas'
    fields= ['nombre' , 'IBU', 'grad_alcohol']
    template_name = "GrupoC/cerveza_list.html"

class CervezaDelete (DeleteView):
    model= Cerveza
    success_url = '/GrupoC/Cervezas/list'
    template_name = "GrupoC/cerveza_list.html"

class CervezaCreate (CreateView):
    model= Cerveza
    success_url = '/GrupoC/Cervezas/list'
    fields= ['nombre' , 'IBU', 'grad_alcohol']
    template_name = "GrupoC/cerveza_form.html"






class CerveceriaList (ListView):
    model= Cerveceria
    template_name = "GrupoC/cerveceria_list.html"

class CerveceriaDetail (DetailView):
    model= Cerveceria
    template_name = "GrupoC/cerveceria_detail.html"

class CerveceriaUpdate (UpdateView):
    model= Cerveceria
    success_url = '/GrupoC/listaCervezas'
    fields= ['nombre' , 'IBU', 'grad_alcohol']
    template_name = "GrupoC/cerveceria_list.html"

class CerveceriaDelete (DeleteView):
    model= Cerveceria
    success_url = '/GrupoC/Cervezas/list'
    template_name = "GrupoC/cerveceria_list.html"

class CerveceriaCreate (CreateView):
    model= Cerveceria
    success_url = '/GrupoC/Cervezas/list'
    fields= ['nombre' , 'IBU', 'grad_alcohol']
    template_name = "GrupoC/cerveceria_form.html"

