from django.urls import path

from . import views

urlpatterns = [
    path('', views.PantallaInicial),
    path('PantallaInicial/', views.PantallaInicial, name='Pantalla Principal'),
    path('PantallaReceta/', views.PantallaReceta, name='PantallaReceta'),
    path('PerfilUsuario/', views.PantallaUsuario, name='Pantalla Perfil Usua'),
    path('PantallaBusqueda/', views.PantallaBusqueda, name='PantallaBusqueda'),
    path('pantallaRegistroReceta/', views.pantallaRegistroReceta, name='pantallaRegistroReceta'),
    path('pantallaRegistroUsuario/', views.pantallaRegistroUsuario, name='pantallaRegistroUsuario'),
    path('PantallaRegistroIngrediente/', views.PantallaRegistroIngrediente, name='PantallaRegistroIngrediente'),
    path('pantallaRegistroComentario/',views.pantallaRegistroComentario,name='pantallaRegistroComentario'),
    path('pantallaVerRecetas/',views.pantallaVerRecetas,name='pantallaVerRecetas'),
    path('pantallaVerIngredientes/',views.pantallaVerIngredientes,name='pantallaVerIngredientes')
]