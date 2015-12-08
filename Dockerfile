FROM ubuntu:latest

#Autor
MAINTAINER Francisco Javier Garrido Mellado <franciscojaviergarridomellado@gmail.com>

#Actualización del Sistema 
RUN sudo apt-get -y update

#Descarga de la aplicación
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/javiergarridomellado/IV_javiergarridomellado.git

# Instalación de Python y PostgreSQL
#RUN sudo apt-get install -y python
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#Instalar la aplicacion

RUN cd IV_javiergarridomellado/ && sudo pip install -r requirements.txt

#Migraciones
RUN cd IV_javiergarridomellado/ && python manage.py syncdb --noinput

