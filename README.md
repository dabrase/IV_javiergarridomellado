# ProyIVDAI_FJGM
Autor: Francisco Javier Garrido Mellado

[![Build Status](https://travis-ci.org/javiergarridomellado/IV_javiergarridomellado.svg?branch=master)](https://travis-ci.org/javiergarridomellado/IV_javiergarridomellado)

[![Build Status](https://snap-ci.com/javiergarridomellado/IV_javiergarridomellado/branch/master/build_image)](https://snap-ci.com/javiergarridomellado/IV_javiergarridomellado/branch/master)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://apuestas.herokuapp.com/)


## Introducción Proyecto Apuestas

Se trata de  una aplicación de apuestas de fútbol donde los usuarios registran unos datos básicos y disponen de un fondo para apostar, se añadiran debates, novedades sobre fútbol, etc. 

Este proyecto será llevado a lo largo del año conjuntamente con la asignatura de Diseño de Aplicaciones para Internet.

[Inscrito en el certamen de Software Libre](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/Pantallazo-Gracias%20-%20Chromium_zpsjdau6lfd.png)

## Seguridad

Respecto a la seguridad se implementará de manera que los datos y credenciales de los usuarios queden salvaguardados de cualquier ataque, para ello será necesario que estos esten separados.

## Infraestructura

Se creará en la nube la infraestructura necesaria para la aplicación, siendo necesario servidores web con su correspondiente balanceador y servidores de bases de datos MySQL replicadas.

Resumen:
-	1.Sistema web donde interaccionan varios usuarios.
-	2.Servidores web con su correspondiente balanceador.
-	3.Base de datos replicadas.


##Herramienta de Construcción

Python permite como herramienta de construcción el uso de archivos *manage.py* y *setup.py* , son los que he usado en mi caso, puede verse en travis como lo uso para la construcción y el posterior testeo.

Además se añaden los archivos [docker_install_and_run](https://github.com/javiergarridomellado/IV_javiergarridomellado/blob/master/docker_install_and_run.sh) y [heroku_deploy](https://github.com/javiergarridomellado/IV_javiergarridomellado/blob/master/heroku_deploy.sh) para la construcción de un entorno seguro (contenedor Docker) y su posterior despliegue automático en el PAAS de Heroku.

## Instalación local de la aplicación

Para ello basta con ejecutar los siguientes comandos:
```
$ git clone https://github.com/javiergarridomellado/IV_javiergarridomellado.git
$ cd IV_javiergarridomellado
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

##Desarrollo basado en pruebas

Para las pruebas he usado el sistema de testeo de Django.Basta con ejecutar el siguiente comando:

**python manage.py test** ó **python manage.py test nombreaplicacion**

Puede verse los correspondientes [tests](https://github.com/javiergarridomellado/IV_javiergarridomellado/blob/master/apu/tests.py) que se realizan.Se usan tanto para **travis** como para **snap-ci**.

![tests](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/tests_zpstcqojtb8.png)

##Integración continua

En este paso se elige un sistema de integración continua de modo que cada cambio que se realice implique una ejecución de los tests mencionados anteriormente, de esta manera se comprueba que la aplicación sigue funcionando correctamente.

En mi caso, he realizado la integración continua con [Travis](https://travis-ci.org/javiergarridomellado/IV_javiergarridomellado) ya que me pareció sencillo y muy completo.
Se ha usado Travis para la integración continua ya que soporta el lenguaje de programación utilizado y permite testear el repositorio de manera facil.

[Más información](https://github.com/javiergarridomellado/IV_javiergarridomellado/blob/master/documentacion/travis.md)

## Despliegue en un Paas Heroku

Me he decantado por Heroku por la facilidad para el despliegue y porque es la que pedían en los ejercicios de la relación.
Esta es la aplicación desplegada en Heroku: [https://apuestas.herokuapp.com/](https://apuestas.herokuapp.com/)

[Más información](https://github.com/javiergarridomellado/IV_javiergarridomellado/blob/master/documentacion/heroku.md)
 

## Entorno de pruebas:[Docker](https://www.docker.com/)

Se usa Docker como plataforma que automatiza el despliegue de la aplicación dentro de contenedores software, de manera que puede probarse en un entorno aislado antes de desplegarla a producción.

La imagen de la aplicación es la [siguiente](https://hub.docker.com/r/javiergarridomellado/iv_javiergarridomellado/)

Para crear el entorno de prueba se ha provisto del archivo **docker_install_and_run.sh**, basta con ejecutar:
```
./docker_install_and_run.sh
```
[Más información](https://github.com/javiergarridomellado/IV_javiergarridomellado/blob/master/documentacion/docker.md)

##Generacion de Documentación
- Ingresar en el directorio **/apu**
- Ejecutar en el terminal **epydoc --html views.py models.py**




