from django.urls import path
from GrupoC import views
from GrupoC.views import CervezaList, CervezaCreate, CervezaDelete, CervezaUpdate, CervezaDetail
from GrupoC.views import CerveceriaList, CerveceriaCreate, ExperienciaCreate, ExperienciaDelete, ExperienciaDetail, ExperienciaList

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Contacto', views.Contacto , name='Contacto'),

    path('listaCervezas', views.CervezaList.as_view(),name='List'),
    path('detalleCervezas/<pk>', views.CervezaDetail.as_view(),name='Detail'),
    path('editarCervezas/<pk>/', views.CervezaUpdate.as_view(),name='Edit'),
    path('borrarCervezas/<pk>', views.CervezaDelete.as_view(),name='Delete'),
    path('nuevaCerveza', views.CervezaCreate.as_view(),name='New'),

    path('listaCervecerias', views.CerveceriaList.as_view(),name='ListCerve'),
    path('nuevaCerveceria', views.CerveceriaCreate.as_view(),name='NewCerve'),
    path('borrarCervezas/<pk>/', views.CervezaDelete.as_view(),name='Delete'),
    
    path('listaExperiencia', views.ExperienciaList.as_view(),name='ListExp'),
    path('detalleExperiencia/<pk>', views.ExperienciaDetail.as_view(),name='DetailExp'),
    path('borrarExperiencia/<pk>/', views.ExperienciaDelete.as_view(),name='DeleteExp'),
    path('nuevaExperiencia', views.ExperienciaCreate.as_view(),name='NewExp'),

]