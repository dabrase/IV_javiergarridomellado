![travis](https://travis-ci.org/javiergarridomellado/IV_javiergarridomellado.svg?branch=master)

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

##Integración continua

Se ha usado Travis para la aplicación continua ya que soporta el lenguaje de programación utilizado y permite testear el repositorio de manera facil.


##Desarrollo basado en pruebas

Para las pruebas he usado el sistema de testeo de Django.Basta con ejecutar el siguiente comando:

**python manage.py test** ó **python manage.py test nombreaplicacion**
