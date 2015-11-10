from django.conf.urls import url
from django.conf.urls import patterns, include

from . import views
from apu.views import raiz, mostrar_navegador
#from .views import RegistrarUsuario, RedirigirUsuario

urlpatterns = [
	url(r'^$', raiz),
	url(r'^navegador/$' ,mostrar_navegador),
	url(r'^registrarusuario/$' , views.RegistrarUsuario.as_view() , name="registrar_usuario" ),
	url(r'^formulariobuscar/$', views.formulario_buscar),
	url(r'^buscar/$', views.buscar), 

    
]
#url(r'^$', views.IndexView.as_view(), name='index'),
