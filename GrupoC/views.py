
from django.http import HttpResponse
from django.shortcuts import render

def Inicio(req):

    return render(req,'GrupoC/inicio.html')

def Cervezas(req):

    return render(req,'GrupoC/cervezas.html')

def Cervecerias(req):

    return render(req,'GrupoC/cervecerias.html')

def Experiencias(req):

    return render(req,'GrupoC/experiencias.html')

    #Aca metemos formulario
    # Si se hace desde un Template va - return render(req,'GrupoC/cerveza.html)