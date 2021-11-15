from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import UsuarioForm, IngredienteForm, RecetaForm
from .models import Question, Receta, Ingrediente, Usuario


def PantallaInicial(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'lista': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def PantallaBusqueda(request):
    vistaBusqueda = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/templateBusqueda.html')
    context = {
        'lista': vistaBusqueda,
    }
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

