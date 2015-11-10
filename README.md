[![Build Status](https://travis-ci.org/javiergarridomellado/IV_javiergarridomellado.svg?branch=master)](https://travis-ci.org/javiergarridomellado/IV_javiergarridomellado)

# ProyIVDAI_FJGM
Francisco Javier Garrido Mellado
##Introducción
Se trata de un proyecto que será llevado a lo largo del año conjuntamente con la asignatura de Diseño de Aplicaciones para Internet. Está basado en un desarrollo web con un framework de alto nivel (Django) donde se interacciona con varios usuarios.En principio tengo pensado hacer una web de apuestas de futbol, donde se registren usuarios, hagan apuestas,debatan, suban videos de futbol, etc.

##Seguridad

Respecto a la seguridad se implementará de manera que los datos y credenciales de los usuarios queden salvaguardados de cualquier ataque, para ello será necesario que estos esten separados.

##Infraestructura

Se creará en la nube la infraestructura necesaria para la aplicación, siendo necesario servidores web con su correspondiente balanceador y servidores de bases de datos MySQL replicadas.

Resumen:
-	1.Sistema web donde interaccionan varios usuarios.
-	2.Servidores web con su correspondiente balanceador.
-	3.Base de datos replicadas.

Inscrito en el certamen:

![foto](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/Pantallazo-Gracias%20-%20Chromium_zpsjdau6lfd.png)

#Segundo hito

## Tecnologías utilizadas

- Se usa framework **Django**, por tanto se desarrolla la aplicación en **Python**
- Base de datos **SQLite**

##Herramienta de Construcción

Python permite como herramienta de construcción el uso de archivos **Makefile**, en mi caso muy similar a lo que se hace en **C** pero enfocado al lenguaje y proyecto utilizado.
- **clean** ,para borrar archivos residuales que se generan como son los *.pyc* y *~py*
- **install** ,con lo que se instala dependencias y paqueteria necesaria para la aplicación.
- **test** , el cual testea la aplicación
- **run** , ejecuta la aplicación.
- **doc** , genera la documentación correspondiente.

###Comandos:
```
make clean
make test
make run
make doc
```

##Desarrollo basado en pruebas

Para las pruebas he usado el sistema de testeo de Django.Basta con ejecutar el siguiente comando:

**python manage.py test** ó **python manage.py test nombreaplicacion**

Aunque para facilitar la elaboracion del testeo lo he incluido dentro del archivo makefile de manera que ejecutando **make test** lo realice. En mi caso el testeo se realiza sobre el modelo de datos que se va a usar.

##Integración continua

Se ha usado Travis para la aplicación continua ya que soporta el lenguaje de programación utilizado y permite testear el repositorio de manera facil.
En mi caso los pasos seguidos han sido:
- Registrarse en la página y sincronizar el repositorio.
- Tener un archivo de testeo de la aplicación.
- Tener archivo makefile que facilite la automatización del testeo,limpieza de archivos, etc.
- Tener un archivo .yml donde se le indica los pasos a seguir para cumplir con la integración continua de manera correcta y eficiente.
- En *github* en el apartado *Setting/Webhooks&services* hay que activar el apartado de *Travis*, seguidamente se pulsa *Test Service*.

##Generacion de Documentación
- Ingresar en el directorio **apuestas/apu**
- Ejecutar en el terminal **epydoc --html views.py models.py**
- O usar la orden **make doc**
