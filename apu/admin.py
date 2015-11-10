from django.contrib import admin
from apu.models import Persona

class PersonaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'dni', 'pais','equipo','hobbies')
	search_fields = ('nombre', 'dni')
	 

admin.site.register(Persona,PersonaAdmin)
# Register your models here.
