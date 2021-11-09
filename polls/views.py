from django.http import HttpResponse
from django.template import loader
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
    vistaBusqueda = Usuario.objects.order_by('-pub_date')[:11]
    template = loader.get_template('polls/templateRegistroUsuario.html')
    context = {
        'lista': vistaBusqueda,
    }
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
