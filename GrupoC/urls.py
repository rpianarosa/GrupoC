from django.urls import path
from GrupoC import views
from GrupoC.views import CervezaList, CervezaCreate, CervezaDelete, CervezaUpdate, CervezaDetail

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Cervezas/', views.Cervezas, name="Cervezas"),
    path('Cervecerias/', views.Cervecerias, name="Cervecerias"),
    path('Experiencias/', views.Experiencias, name="Experiencias"),

    path('listaCervezas', views.CervezaList.as_view(),name='List'),
    path('detalleCervezas/<pk>/', views.CervezaDetail.as_view(),name='Detail'),
    path('editarCervezas/<pk>/', views.CervezaUpdate.as_view(),name='Edit'),
    path('borrarCervezas/<pk>/', views.CervezaDelete.as_view(),name='Delete'),
    path('nuevaCervezas', views.CervezaCreate.as_view(),name='New')
]