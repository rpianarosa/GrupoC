from http.client import HTTPResponse
from django.shortcuts import render

def Cerveza(req):

    return HTTPResponse('Estoy en la parte de cervezas')

    #Aca metemos formulario