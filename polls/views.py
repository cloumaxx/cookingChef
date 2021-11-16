from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.db.models import Q
from .forms import UsuarioForm, IngredienteForm, RecetaForm, ComentarioForm
from .models import Receta, Ingrediente, Usuario


def PantallaInicial(request):
    template = loader.get_template('polls/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def PantallaBusqueda(request):
    queryset = request.GET.get("busqueda")
    receta = Receta.objects.all()
    if queryset:
        receta = Receta.objects.filter(
            Q(titulo__icontains=queryset)
        ).distinct()
    return render(request, 'polls/templateBusqueda.html', {'Receta': receta})


def pantallaVerIngredientes(request):
    ingrediente= Ingrediente.objects.all()
    contexto = {
        'ingredientes':ingrediente
    }
    return render(request,'polls/templateTodosIngredientes.html',contexto)


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


def pantallaRegistroUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Pantalla Principal')
    else:
        form = UsuarioForm()
    return render(request, 'polls/templateRegistroUsuario.html', {'form': form})
    return HttpResponse(template.render(context, request))


def PantallaRegistroIngrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Pantalla Principal')
    else:
        form = IngredienteForm()
    return render(request, 'polls/templateRegistroIngrediente.html', {'form': form})
    return HttpResponse(template.render(context, request))


def pantallaRegistroReceta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Pantalla Principal')
    else:
        form = RecetaForm()
    return render(request, 'polls/templateRegistroReceta.html', {'form': form})
    return HttpResponse(template.render(context, request))


def PantallaUsuario(request):
    return HttpResponse("esta pantalla se encargara de mostrar el perfil de un usuario")


def PantallaReceta(request):
    return HttpResponse("esta pantalla se encargara de mostrar la informacion referente a una receta")
