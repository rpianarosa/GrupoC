from django.urls import path
from GrupoC import views
from GrupoC.views import CervezaList, CervezaCreate, CervezaDelete, CervezaUpdate, CervezaDetail
from GrupoC.views import CerveceriaList, CerveceriaCreate, CerveceriaDelete, CerveceriaUpdate, CerveceriaDetail

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Cervezas/', views.Cervezas, name="Cervezas"),
    path('Cervecerias/', views.Cervecerias, name="Cervecerias"),
    path('Experiencias/', views.Experiencias, name="Experiencias"),

    path('listaCervezas', views.CervezaList.as_view(),name='List'),
    path('detalleCervezas/<pk>', views.CervezaDetail.as_view(),name='Detail'),
    path('editarCervezas/<pk>/', views.CervezaUpdate.as_view(),name='Edit'),
    path('borrarCervezas/<pk>/', views.CervezaDelete.as_view(),name='Delete'),
    path('nuevaCerveza', views.CervezaCreate.as_view(),name='New'),

    path('listaCervecerias', views.CerveceriaList.as_view(),name='ListCerve'),
    path('detalleCerveceria/<pk>/', views.CerveceriaDetail.as_view(),name='DetailCerve'),
    path('editarCerveceria/<pk>/', views.CerveceriaUpdate.as_view(),name='EditCerve'),
    path('borrarCerveceria/<pk>/', views.CerveceriaDelete.as_view(),name='DeleteCerve'),
    path('nuevaCerveceria', views.CerveceriaCreate.as_view(),name='NewCerve')
]