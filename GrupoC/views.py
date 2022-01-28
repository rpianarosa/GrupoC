
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from GrupoC.models import Cerveza, Cerveceria, Experiencia

from django import forms
from datetime import date

def PreInicio(req):

    return render(req,'GrupoC/preinicio.html')

def Inicio(req):

    return render(req,'GrupoC/padre2.html')

def Contacto(req):

    return render(req,'GrupoC/contacto.html')

def Acercade(req):

    return render(req,'GrupoC/acercade.html')

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
    template_name = "GrupoC/experiencias_list.html"

class ExperienciaUpdate (UpdateView):
    model= Experiencia
    success_url = '/Cerveblog/listaExperiencia'
    fields= ['nombre' , 'apellido', 'cerv_tomada', 'cerv_atend', 'punt_cerveza', 'punt_cerveceria']
    template_name = "GrupoC/experiencia_form.html"

class ExperienciaDelete (DeleteView):
    model= Experiencia
    success_url = '/Cerveblog/listaExperiencia'
    template_name = "GrupoC/experiencia_conf_delete.html"

class ExperienciaCreate (CreateView):
    model= Experiencia
    success_url = '/Cerveblog/listaExperiencia'
    fields= ['nombre' , 'apellido', 'cerv_tomada', 'cerv_atend', 'punt_cerveza', 'punt_cerveceria']
    template_name = "GrupoC/experiencia_form.html"


class FechaForm(forms.Form):
    intro_fecha= forms.DateField()
    

def calcular_edad(intro_fecha):
    dif= date.today() - intro_fecha

    if dif < 18:    
        return ("No cumple con la edad requerida para ingresar")
    
    else:
        return render('GrupoC/inicio.html')
    
