
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from GrupoC.models import Cerveza, Cerveceria, Experiencia

from django import forms
from datetime import date

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from GrupoC.forms import UserEditForm 

from django.core.mail import send_mail
from django.conf import settings

def PreInicio(req):
    return render(req,'GrupoC/preinicio.html')

def Inicio(req):
    if(req.method=='POST'):
        if (len(req.POST['date']) > 0):
            dato=date.fromisoformat(req.POST['date'])
            dif=date.today() - dato
            edad=(dif.days/365)

            if (edad>18):
                return render(req, 'GrupoC/padre2.html')
            else:
                return render(req, 'GrupoC/preinicio.html', {'error': "Para poder ingresar debes ser mayor de edad"})
        else:
            return render (req, 'GrupoC/preinicio.html', {'error':"Debes ingresar una fecha válida"})

    return render(req,'GrupoC/padre2.html')

def Contacto(request):
    if request.method=="POST":
        subject=request.POST["nombre"]
        message=request.POST["mensaje"] + " " + request.POST["mail"]
        email_form=settings.EMAIL_HOST_USER
        recipiente=["cerveblog@gmail.com"]
        send_mail(subject,message,email_form,recipiente)
        return render(request, 'GrupoC/contacto.html')
    
        
    return render(request,'GrupoC/contacto.html')

def Acercade(req):

    return render(req,'GrupoC/acercade.html')

class CervezaList (ListView):
    model= Cerveza
    template_name = "GrupoC/cerveza_list.html"

class CervezaDetail (DetailView):
    model= Cerveza
    template_name = "GrupoC/cerveza_detail.html"

class CervezaUpdate (LoginRequiredMixin, UpdateView):
    model= Cerveza
    success_url = '/Cerveblog/listaCervezas'
    fields= ['nombre' , 'IBU', 'grad_alcohol']
    template_name = "GrupoC/cerveza_form.html"

class CervezaDelete (LoginRequiredMixin, DeleteView):
    model= Cerveza
    success_url = '/Cerveblog/listaCervezas'
    template_name = "GrupoC/cerveza_conf_delete.html"

class CervezaCreate (LoginRequiredMixin, CreateView):
    model= Cerveza
    success_url = '/Cerveblog/listaCervezas'
    fields= ['nombre' , 'IBU', 'grad_alcohol']
    template_name = "GrupoC/cerveza_form.html"




class CerveceriaList (ListView):
    model= Cerveceria
    template_name = "GrupoC/cerveceria_list.html"
class CerveceriaCreate (LoginRequiredMixin, CreateView):
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

class ExperienciaCreate (LoginRequiredMixin, CreateView):
    model= Experiencia
    success_url = '/Cerveblog/listaExperiencia'
    fields= ['nombre' , 'apellido', 'cerv_tomada', 'cerv_atend', 'punt_cerveza', 'punt_cerveceria']
    template_name = "GrupoC/experiencia_form.html"


def busquedaCerveza(request):
    return render(request, 'GrupoC/busqueda_cerveza.html')

def buscar(request):
    if request.GET["cerveza"]:
        nombre = request.GET["cerveza"] 
        cerveza = Cerveza.objects.filter(nombre__icontains=nombre)
        return render(request, "GrupoC/resultados_busqueda.html", {"cerveza":cerveza, "nombre":nombre})

    else: 
        mensaje='Cerveza no encontrada'
    return render(request, "GrupoC/resultados_busqueda.html", {mensaje})

    
    

def login_request (request):
    if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')
                user = authenticate(username=usuario, password=contra)
                if user is not None:
                    login(request, user)
                    return render(request,"GrupoC/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                else:
                    return render(request,"GrupoC/iniciofallido.html", {"mensaje":f"Contraseña incorrecta"} )
            else:
                    return render(request,"GrupoC/iniciofallido.html" ,  {"mensaje":f"Usuario incorrecto"})
    form = AuthenticationForm()
    return render(request,"GrupoC/login.html", {'form':form} )

def registro(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data['username']
            form.save()
            return render(request, "GrupoC/inicio.html" , {"mensaje":f"Usuario {username} creado, ahora ingresa con tus datos"})
        else:
            return render(request, "GrupoC/registrofallido.html" , {"mensaje":f"Algun dato es incorrecto"})
    
    form =UserCreationForm()
    return render(request, "GrupoC/registro.html" , {"form":form})


def editarPerfil(request):

    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST) 
        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data
            usuario.user = informacion['user']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()
            return render(request, "GrupoC/inicio.html", {"mensaje":f"Usuario {usuario.user} modificado"})
        else:
            return render(request, "GrupoC/editarPerfil.html" , {"mensaje":f"Algun dato es incorrecto"})
    else: 
        miFormulario= UserEditForm(initial= {'username':usuario.username})

        return render(request, "GrupoC/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})






def urlImagen():

    return "/media/avatares/logo.png"



