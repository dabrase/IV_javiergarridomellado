from django.shortcuts import render
from django.http import HttpResponse 
from apu.models import Persona
from django.views.generic import CreateView, TemplateView, ListView
import datetime
from django.views import generic

# Create your views here.
def raiz(request):
	"""Funcion que da la hora actual
	"""
	ahora = datetime.datetime.now()
	return render(request,'indice.html',{'fecha_actual':ahora})

def mostrar_navegador(request):
	"""Muestra navegador usado
	"""
	try:
		ua = request.META['HTTP_USER_AGENT']
	except KeyError:
		ua = 'unknown'
	return HttpResponse("Tu navegador es %s" % ua) 
	
def formulario_buscar(request):
	"""Busca persona en la base datos
	"""
	return render(request,'formulario_buscar.html')



class RegistrarUsuario(CreateView):
	"""No funciona corregir
	"""
	model = Persona
	template_name = 'registrarusuario.html'
	
	#success_url = reverse_lazy('redirigir_empresa')

class RedirigirUsuario(ListView):
	"""No funciona, corregir
	"""
	template_name = 'redirigirusuario.html'
	model = Persona
	context_object_name = 'personas'

def buscarr(request): 
 
    if 'dni' in request.GET and 'nombre' in request.GET and request.GET['dni'] and request.GET['nombre']: 
        mensaje = 'Estas buscando a %r ' %request.GET['nombre'] + 'con DNI: %r ' %  request.GET['dni'] 
    else: 
        mensaje = 'Haz subido un formulario vacio.' 
    return HttpResponse(mensaje)

def buscar(request):
	"""Busca personas segun parametros GET
	"""
	if 'dni' in request.GET and request.GET['dni']:
		dni = request.GET['dni']
		personas = Persona.objects.filter(dni__icontains=dni)
		return render(request,'resultados.html',  {'personas': personas, 'query': dni})
	else:
		return HttpResponse('Por favor introduce un termino de busqueda.') 
