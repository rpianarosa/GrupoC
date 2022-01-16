from django.urls import path
from GrupoC import views

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Cervezas/', views.Cervezas, name="Cervezas"),
    path('Cervecerias/', views.Cervecerias, name="Cervecerias"),
    path('Experiencias/', views.Experiencias, name="Experiencias")
]