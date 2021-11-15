from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import UsuarioForm
from .models import Question, Receta, Ingrediente, Usuario
from django.db import connection

def calcularCodigoUsua():
    with connection.cursor() as cursor:
        cursor.execute('SELECT  MAX("idUsuario") \n FROM public.polls_usuario;')
        row = cursor.fetchone()
    aux = str(row)
    num = int(aux[2])
    final = num + 1

    return final
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


def pantallaRegistroReceta(request):
    vistaBusqueda = Receta.objects.order_by('-pub_date')[:5]

    template = loader.get_template('polls/templateRegistroReceta.html')
    context = {
        'lista': vistaBusqueda,
    }
    return HttpResponse(template.render(context, request))


def PantallaUsuario(request):
    return HttpResponse("esta pantalla se encargara de mostrar el perfil de un usuario")


def PantallaReceta(request):
    return HttpResponse("esta pantalla se encargara de mostrar la informacion referente a una receta")
