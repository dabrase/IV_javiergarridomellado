from django.db import models
#Para generar la documentacion ejecutar epydoc --html views.py models.py (sale error pero genera los html)
# Create your models here.

class Persona(models.Model):
	"""Modelo del registro Persona.
		Sirve para definir en la base de datos
	"""

	nombre = models.CharField(max_length=50)
	dni = models.CharField(max_length=9)
	pais = models.CharField(max_length=20)
	equipo = models.CharField(max_length=10)
	hobbies = models.TextField(max_length=200)

	def __unicode__(self):
		return self.nombre
