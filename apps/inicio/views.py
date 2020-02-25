from django.views.generic import View, TemplateView, ListView
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Autor, Doctor, Noticia, Evento, Documento

# Create your views here.


def inicio(request):
    noticias = Noticia.objects.filter(eliminado=False)[:3]
    return render(request, 'index.html', {'noticias': noticias})


def detalle_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'pages/noticia_detalle.html', {'noticia': noticia})

def detalle_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, 'pages/evento_detalle.html', {'evento': evento})

def caso_del_mes(request, id):
    documento = get_object_or_404(Documento, id=id)
    return render(request, 'pages/caso_del_mes.html', {'documento': documento})

class Noticias(ListView):
    model = Noticia
    template_name = 'pages/noticias.html'
    context_object_name = 'noticias'
    queryset = model.objects.filter(eliminado=False)
    paginate_by = 6

class Casos(ListView):
    model = Documento
    template_name = 'pages/casos.html'
    context_object_name = 'documentos'
    queryset = model.objects.filter(eliminado=False)
    paginate_by = 6

class Actividades(ListView):
    model = Evento
    template_name = 'pages/actividades.html'
    context_object_name = 'eventos'
    queryset = model.objects.filter(eliminado=False)
    paginate_by = 6

class Doctores(ListView):
    model = Doctor
    template_name = 'pages/doctores.html'
    context_object_name = 'doctores'
    queryset = model.objects.filter(eliminado=False, directivo=True)
    paginate_by = 8


class Expresidentes(ListView):
    model = Doctor
    template_name = 'pages/expresidentes.html'
    context_object_name = 'expresidentes'
    queryset = model.objects.filter(
        eliminado=False, expresidente=True)
    paginate_by = 8


class Miembros(ListView):
    model = Doctor
    template_name = 'pages/miembros.html'
    context_object_name = 'miembros'
    queryset = model.objects.filter(
        eliminado=False, miembro=True)
    paginate_by = 8


class Nosotros(TemplateView):
    template_name = 'pages/nosotros.html'

class EstatutoAntiguo(TemplateView):
    template_name = 'pages/estatutos/estatuto_antiguo.html'

class EstatutoSociedad(TemplateView):
    template_name = 'pages/estatutos/estatuto_sociedad.html'

class ReformaEstatutos(TemplateView):
    template_name = 'pages/estatutos/reforma_estatuto.html'
