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
- Base de datos **SQLite**

##Herramienta de Construcción

Python permite como herramienta de construcción el uso de archivos *manage.py* y *setup.py* , son los que he usado en mi caso, puede verse en travis como lo uso para el testeo.


##Desarrollo basado en pruebas

Para las pruebas he usado el sistema de testeo de Django.Basta con ejecutar el siguiente comando:

**python manage.py test** ó **python manage.py test nombreaplicacion**

Aunque para facilitar la elaboracion del testeo lo he incluido dentro del archivo makefile de manera que ejecutando **make test** lo realice. En mi caso el testeo se realiza sobre el modelo de datos que se va a usar.

##Integración continua

Se ha usado Travis para la aplicación continua ya que soporta el lenguaje de programación utilizado y permite testear el repositorio de manera facil.
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

La aplicacion [desplegada](https://apuestas.herokuapp.com/)

Se añade ademas un proceso de integración continua junto al despliegue mediante [Snap-CI](https://snap-ci.com)



