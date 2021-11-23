from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from django.db.models import Q
from .forms import UsuarioForm, IngredienteForm, RecetaForm, ComentarioForm, UsuarioIngrForm
from .models import Receta, Ingrediente, Usuario


def PantallaInicial(request):
    receta = Receta.objects.all()
    contexto = {
        'recetas': receta
    }
    return render(request, 'polls/templatePantallaInicial.html', contexto)


def pantallaVerIngredientes(request):
    ingrediente = Ingrediente.objects.all()
    contexto = {
        'ingredientes': ingrediente
    }
    return render(request, 'polls/templateTodosIngredientes.html', contexto)


# esta pantalla muestra el listado de pantallas registradas
def pantallaVerRecetas(request):
    receta = Receta.objects.all()
    contexto = {
        'recetas': receta
    }
    return render(request, 'polls/templateTodasRecetas.html', contexto)


def pantallaIngreso(request):
    if request.method == 'POST':
        form = UsuarioIngrForm(request.POST)
        if form.is_valid():
            form.clean_Ingreso()
            print('entro')
        return redirect('Pantalla Principal')
    elif request.method == 'NUEVO':
        return redirect(request, 'polls/templateRegistroUsuario.html')
    else:
        form = UsuarioIngrForm()
    return render(request, 'polls/templateIngreso.html', {'form': form})
    return HttpResponse(template.render(context, request))


def pantallaBusqueda(request):
    buscarRec = request.GET.get("busquedaReceta")
    buscarUsua = request.GET.get('busquedaUsuario')
    buscarIngr = request.GET.get('busquedaIngrediente')
    recetas = Receta.objects.all()
    ingredientes = Ingrediente.objects.all()
    usuarios = Usuario.objects.all()
    if buscarRec:
        recetas = Receta.objects.filter(
            Q(titulo__icontains=buscarRec) |
            Q(ingredientes__icontains=buscarRec) |
            Q(creador__icontains=buscarRec) |
            Q(calificacion__icontains=buscarRec) |
            Q(descripcion__icontains=buscarRec)
        ).distinct()
        return render(request, 'polls/indicesBusquedas/templateIndiceBusquedaReceta.html', {'recetas': recetas})
    elif buscarIngr:
        ingredientes = Ingrediente.objects.filter(
            Q(nombre__icontains=buscarIngr) |
            Q(descripcion__icontains=buscarIngr) |
            Q(zonaOrigen__icontains=buscarIngr) |
            Q(clasificacion__icontains=buscarIngr)
        ).distinct()
        return render(request, 'polls/indicesBusquedas/templateIndiceBusquedaIngrediente.html',
                      {'ingredientes': ingredientes})
    elif buscarUsua:
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=buscarUsua) |
            Q(apellido__icontains=buscarUsua) |
            Q(apodo__icontains=buscarUsua) |
            Q(cedula__icontains=buscarUsua) |
            Q(email__icontains=buscarUsua)
        ).distinct()
        return render(request, 'polls/indicesBusquedas/templateIndiceBusquedaUsuario.html', {'usuarios': usuarios})
    return render(request, 'polls/templateBusqueda.html', {'usuarios': usuarios})


def pantallaIndiceReceta(request, recetas):
    return render(request, 'polls/templateBusqueda.html', {'recetas': recetas})


# esta panatalla es para registrar un comentario
def pantallaRegistroComentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Pantalla Principal')
    else:
        form = ComentarioForm()
    return render(request, 'polls/templeateCrearComentario.html', {'form': form})
    return HttpResponse(template.render(context, request))


def pantallaRegistroUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('pantallaIngreso')
    else:
        form = UsuarioForm()
    return render(request, 'polls/templateRegistroUsuario.html', {'form': form})
    return HttpResponse(template.render(context, request))


def PantallaRegistroIngrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Pantalla Principal')
    else:
        form = IngredienteForm()
    return render(request, 'polls/templateRegistroIngrediente.html', {'form': form})
    return HttpResponse(template.render(context, request))


def pantallaRegistroReceta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Pantalla Principal')
    else:
        form = RecetaForm()
    return render(request, 'polls/templateRegistroReceta.html', {'form': form})
    return HttpResponse(template.render(context, request))


def PantallaUsuario(request):
    usuario = Usuario.objects.all()
    contexto = {
        'usuarios': usuario
    }
    return render(request, 'polls/templateVerPerfil.html', contexto)


def PantallaIngrediente(request):
    ingrediente = Ingrediente.objects.all()
    contexto = {
        'ingredientes': ingrediente
    }
    return render(request, 'polls/templateVerIngrediente.html', contexto)


def PantallaReceta(request):
    receta = Receta.objects.all()
    contexto = {
        'recetas': receta
    }
    return render(request, 'polls/templateReceta.html', contexto)
