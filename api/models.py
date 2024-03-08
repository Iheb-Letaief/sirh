
from django.db import models
from employees.models import Agent
from payrolls.models import Paie



class Declaration(models.Model):
    agent = models.ForeignKey(Agent, related_name='declarations', on_delete=models.CASCADE, null=True)
    paies = models.ManyToManyField(Paie, related_name='paies_declarations')
    titre_declaration = models.CharField(max_length=255)
    type_declaration = models.CharField(max_length=255)
    pourcentage = models.FloatField()
    montant = models.FloatField()
    date_declaration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre_declaration

