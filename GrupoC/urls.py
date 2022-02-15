from django.urls import path
from GrupoC import views
from GrupoC.views import CervezaList, CervezaCreate, CervezaDelete, CervezaUpdate, CervezaDetail
from GrupoC.views import CerveceriaList, CerveceriaCreate, ExperienciaCreate, ExperienciaDelete, ExperienciaUpdate, ExperienciaList
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Contacto', views.Contacto , name='Contacto'),
    path('Acercade', views.Acercade , name='Acercade'),

    path('listaCervezas', views.CervezaList.as_view(),name='List'),
    path('detalleCervezas/<pk>', views.CervezaDetail.as_view(),name='Detail'),
    path('editarCervezas/<pk>/', views.CervezaUpdate.as_view(),name='Edit'),
    path('borrarCervezas/<pk>', views.CervezaDelete.as_view(),name='Delete'),
    path('nuevaCerveza', views.CervezaCreate.as_view(),name='New'),

    path('listaCervecerias', views.CerveceriaList.as_view(),name='ListCerve'),
    path('nuevaCerveceria', views.CerveceriaCreate.as_view(),name='NewCerve'),
    path('borrarCervezas/<pk>/', views.CervezaDelete.as_view(),name='Delete'),
    
    path('listaExperiencia', views.ExperienciaList.as_view(),name='ListExp'),
    path('editarExperiencia/<pk>', views.ExperienciaUpdate.as_view(),name='EditExp'),
    path('borrarExperiencia/<pk>/', views.ExperienciaDelete.as_view(),name='DeleteExp'),
    path('nuevaExperiencia', views.ExperienciaCreate.as_view(),name='NewExp'),

    path('Login', views.login_request, name='Login'),
    path('Registro', views.registro, name='Registro'),
    path('Logout', LogoutView.as_view(template_name='GrupoC/logout.html'), name='Logout'),

    path('editarPerfil', views.editarPerfil, name="editarPerfil"),

    path('busquedaCerveza', views.busquedaCerveza, name="BusquedaCerveza"),
    path('buscar/', views.buscar, name='Buscar')




]