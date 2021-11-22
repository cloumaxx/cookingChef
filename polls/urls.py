from django.urls import path, re_path

from cookingFinal.settings import MEDIA_ROOT
from . import views
from django.views.static import serve

urlpatterns = [

    path('', views.PantallaInicial),#views.pantallaIngreso),
    path('pantallaIngreso',views.pantallaIngreso,name='pantallaIngreso'),
    path('PantallaInicial/', views.PantallaInicial, name='Pantalla Principal'),
    path('PantallaReceta/', views.PantallaReceta, name='PantallaReceta'),
    path('PerfilUsuario/', views.PantallaUsuario, name='Pantalla Perfil Usua'),
    path('PantallaBusqueda/', views.PantallaBusqueda, name='PantallaBusqueda'),
    path('pantallaRegistroReceta/', views.pantallaRegistroReceta, name='pantallaRegistroReceta'),
    path('pantallaRegistroUsuario/', views.pantallaRegistroUsuario, name='pantallaRegistroUsuario'),
    path('PantallaRegistroIngrediente/', views.PantallaRegistroIngrediente, name='PantallaRegistroIngrediente'),
    path('pantallaRegistroComentario/', views.pantallaRegistroComentario, name='pantallaRegistroComentario'),
    path('pantallaVerRecetas/', views.pantallaVerRecetas, name='pantallaVerRecetas'),
    path('pantallaVerIngredientes/', views.pantallaVerIngredientes, name='pantallaVerIngredientes'),
    path('PantallaIngrediente/',views.PantallaIngrediente,name='PantallaIngrediente'),
    path('pantallaBusqueda/',views.pantallaBusqueda,name='pantallaBusqueda'),
]