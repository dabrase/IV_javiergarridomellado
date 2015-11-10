from django.test import TestCase

# Create your tests here.

from apu.models import Persona

class PersonaMethodTests(TestCase):

	def test_nombre_persona(self):
		per = Persona(nombre='Jose' ,dni='45678921r',pais='Holanda',equipo='Betis',hobbies='musica')
		per.save()
		self.assertEqual(per.nombre,'Jose')
		self.assertEqual(per.dni,'45678921r')
		self.assertEqual(per.pais,'Holanda')
		self.assertEqual(per.equipo,'Betis')
		self.assertEqual(per.hobbies,'musica')
		print("Testeo correcto.")
