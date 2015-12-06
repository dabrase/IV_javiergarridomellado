# Integración continua con Travis

Para el uso de Travis los pasos seguidos han sido:
- Registrarse en la página y sincronizar el repositorio.
- Tener un archivo de testeo de la aplicación.
- Tener archivo manage.py que facilite la automatización del testeo.
- Tener un archivo .yml donde se le indica los pasos a seguir para cumplir con la integración continua de manera correcta y eficiente.
- En *github* en el apartado *Setting/Webhooks&services* hay que activar el apartado de *Travis*, seguidamente se pulsa *Test Service*.

El contenido del archivo *.travis.yml* es el siguiente:
```
language: python
python:
 - "2.7"

install:
 - pip install -r requirements.txt
script:
 - python manage.py test 
```
Por último una captura de una modificación realizada al código del repositorio:

![travis](http://i1045.photobucket.com/albums/b457/Francisco_Javier_G_M/travis_zpsjqr6xhcs.png)
