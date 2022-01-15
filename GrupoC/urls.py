from django.urls import path
from GrupoC import views

urlpatterns = [
    path('Cervezas', views.Cerveza),
]