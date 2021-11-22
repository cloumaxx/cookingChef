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
    """template = loader.get_template('polls/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))"""


def PantallaBusqueda(request):
    queryset = request.GET.get("busqueda")
    receta = Receta.objects.all()
    if queryset:
        receta = Receta.objects.filter(
            Q(titulo__icontains=queryset)
        ).distinct()
    return render(request, 'polls/templateBusqueda.html', {'Receta': receta})


def pantallaVerIngredientes(request):
    ingrediente = Ingrediente.objects.all()
    contexto = {
        'ingredientes': ingrediente
    }
    return render(request, 'polls/templateTodosIngredientes.html', contexto)


def pantallaVerRecetas(request):
    receta = Receta.objects.all()
    contexto = {
        'recetas': receta
    }
    return render(request, 'polls/templateTodasRecetas.html', contexto)


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
        return redirect('PantallaInicial')
    else:
        form = IngredienteForm()
    return render(request, 'polls/templateRegistroIngrediente.html', {'form': form})
    return HttpResponse(template.render(context, request))


def pantallaBusqueda(request):
    buscar = request.GET.get("busqueda")
    recetas = Receta.objects.all()
    if buscar:
        recetas = Receta.objects.filter(
            Q(titulo__icontains=buscar) |
            Q(ingredientes__icontains=buscar) |
            Q(creador__icontains=buscar) |
            Q(calificacion__icontains=buscar) |
            Q(descripcion__icontains=buscar)
        ).distinct()

    return render(request, 'polls/templateTodasRecetas.html',{'recetas':recetas})


def pantallaRegistroReceta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('PantallaInicial')
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
