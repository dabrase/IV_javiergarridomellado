[![Build Status](https://travis-ci.org/javiergarridomellado/IV_javiergarridomellado.svg?branch=master)](https://travis-ci.org/javiergarridomellado/IV_javiergarridomellado)

[![Build Status](https://snap-ci.com/javiergarridomellado/IV_javiergarridomellado/branch/master/build_image)](https://snap-ci.com/javiergarridomellado/IV_javiergarridomellado/branch/master)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://apuestas.herokuapp.com/)

# ProyIVDAI_FJGM
Francisco Javier Garrido Mellado

##Introducción Proyecto Apuestas
Estoy haciendo una app de apuestas de futbol donde los usuarios registran unos datos basicos y disponen de un fondo para apostar, se añadiran debates, novedades sobre futbol, etc. Ahora mismo esta en fase básica.

Este proyecto será llevado a lo largo del año conjuntamente con la asignatura de Diseño de Aplicaciones para Internet.

##Seguridad

Respecto a la seguridad se implementará de manera que los datos y credenciales de los usuarios queden salvaguardados de cualquier ataque, para ello será necesario que estos esten separados.

##Infraestructura

Se creará en la nube la infraestructura necesaria para la aplicación, siendo necesario servidores web con su correspondiente balanceador y servidores de bases de datos MySQL replicadas.

Resumen:
-	1.Sistema web donde interaccionan varios usuarios.
-	2.Servidores web con su correspondiente balanceador.
-	3.Base de datos replicadas.

Inscrito en el certamen de SL:

![foto](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/Pantallazo-Gracias%20-%20Chromium_zpsjdau6lfd.png)


## Tecnologías utilizadas

- Se usa framework **Django**, por tanto se desarrolla la aplicación en **Python**
- Base de datos **SQLite** para pruebas en local.
- Base de datos **PostgreSQL** en el PaaS Heroku.

##Herramienta de Construcción

Python permite como herramienta de construcción el uso de archivos *manage.py* y *setup.py* , son los que he usado en mi caso, puede verse en travis como lo uso para la construccion y el posterior testeo.


##Desarrollo basado en pruebas

Para las pruebas he usado el sistema de testeo de Django.Basta con ejecutar el siguiente comando:

**python manage.py test** ó **python manage.py test nombreaplicacion**

Aunque para facilitar la elaboracion del testeo lo he incluido dentro del archivo makefile de manera que ejecutando **make test** lo realice. En mi caso el testeo se realiza sobre el modelo de datos que se va a usar.

Esto se usa tanto para **travis** como para **snap-ci**.

##Integración continua

Se ha usado Travis para la integración continua ya que soporta el lenguaje de programación utilizado y permite testear el repositorio de manera facil.
En mi caso los pasos seguidos han sido:
- Registrarse en la página y sincronizar el repositorio.
- Tener un archivo de testeo de la aplicación.
- Tener archivo manage.py que facilite la automatización del testeo.
- Tener un archivo .yml donde se le indica los pasos a seguir para cumplir con la integración continua de manera correcta y eficiente.
- En *github* en el apartado *Setting/Webhooks&services* hay que activar el apartado de *Travis*, seguidamente se pulsa *Test Service*.

##Generacion de Documentación
- Ingresar en el directorio **/apu**
- Ejecutar en el terminal **epydoc --html views.py models.py**

## Despliegue en un Paas Heroku

Me he decantado por Heroku por la facilidad para el despliegue y porque es la que pedían en los ejercicios de la relación. Para su despliegue he necesitado de los siguientes ficheros de definición:
- Procfile ( para que Heroku sepa que tiene que lanzar, usa gunicorn )
```
web: gunicorn apuestas.wsgi --log-file -
```

- runtime.txt ( por si hay algun problema compatibilidad con Python )
```
python-2.7.6
```
- requirements.txt ( se define todo lo necesario para lanzar la app )
```
Django==1.8.6
argparse==1.2.1
dj-database-url==0.3.0
dj-static==0.0.6
django-toolbelt==0.0.1
djangorestframework==3.3.1
foreman==0.9.7
futures==3.0.3
gunicorn==19.3.0
psycopg2==2.6.1
requests==2.8.1
requests-futures==0.9.5
static3==0.6.1
wheel==0.26.0
whitenoise==2.0.4
wsgiref==0.1.2
```
Puede verse que tambien se dispone de **whitenoise** para archivos estaticos, queda definido en **setting.py** para su uso si se requiere.
Tras el registro en Heroku hay que ejecutar una serie de comandos para tener apunto el despliegue:
```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   
heroku login
heroku create
git add .
git commit -m "subida"
heroku apps:rename apuestas
git push heroku master
```
He usado la base de datos **PostgreSQL** que proporciona **Heroku** para el despliegue, en local sigo usando **SQLite**, lo he realizado con estos pasos:
- Teniendo *psycopg2* para poder usar dicha base de datos.
- Tener instalado *dj_database_url*, tambien necesario para PostgreSQL.
- Abrir el archivo *setting.py* del proyecto y añadir lo siguiente( sacado del siguiente [enlace](http://stackoverflow.com/questions/26080303/improperlyconfigured-settings-databases-is-improperly-configured-please-supply):
```
import dj_database_url

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ON_HEROKU = os.environ.get('PORT')
if ON_HEROKU:
	DATABASE_URL='postgres://url_de_mi_bd'
	DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
- En **wsgi.py** poner lo siguiente:
```
import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apuestas.settings")

#from whitenoise.django import DjangoWhiteNoise
application = get_wsgi_application()


application = Cling(get_wsgi_application())
#application = DjangoWhiteNoise(application)
```
- Notar que en DATABASE_URL se pone la url que sale para la base de datos postgreSQL que Heroku nos ofrece, hay que darle a show para verlo.
- Subir cambios a github y hacer **git push heroku master**.
- Ejecutar los comando **heroku run python manage.py makemigrations**, **heroku run python manage.py migrate** y **heroku run python manage.py createsuperuser** para sincronizar la base de datos PostgreSQL.
 

La aplicacion [desplegada](https://apuestas.herokuapp.com/)

Se añade ademas un proceso de integración continua junto al despliegue mediante [Snap-CI](https://snap-ci.com).Desde la interfaz web realizo la siguiente configuración:

![paso1](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/snap1_zpsgowrqt6s.png)

![paso2](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/snaptest_zpsjmbr7ezk.png)

![paso3](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/snapdespliegue_zpsgoc8n8bo.png)

![resultados1](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/snappasantest_zpstn0bgbtl.png)

![resultados2](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/snaptest2_zps2t6125ue.png)

![resultados3](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/snapdespliegue2_zpsgmdw0np4.png)

Con todo esto queda realizado la integración continua, cada vez que se haga un push al repositorio se pasan los tests y si son satisfactorio se levanta la app.

##Avances

Un avance significativo es el de usar JSON con sus correspondientes tests.Puede verse la clase en el archivo *views.py*, su uso en *tests.py* y el correspondiente archivo *serializers.py*.

Ademas se añaden varias vistas mas a la aplicación, puede verse en la página principal algunos enlaces que nos llevan a diferentes páginas.Consultando *urls.py* puede verse todas las páginas disponibles.


#
