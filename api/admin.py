from django.contrib import admin

from .models import Agent, Poste, Paie, Contrat, Prime, Declaration

# Register your models here.
admin.site.register(Agent)
admin.site.register(Poste)
admin.site.register(Paie)
admin.site.register(Contrat)
admin.site.register(Prime)
admin.site.register(Declaration)