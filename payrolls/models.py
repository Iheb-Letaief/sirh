from django.db import models
from employees.models import Agent
# Create your models here.

class Paie(models.Model):
    agent = models.ForeignKey(Agent, related_name='paies', on_delete=models.CASCADE, null=True, blank=True)
    titre_paie = models.CharField(max_length=255)
    date_remboursement = models.DateTimeField(auto_now_add=True)
    salaire_mois = models.FloatField()
    salaire_annee = models.FloatField()
    #salaire_brute = models.FloatField()
    #salaire_net = models.FloatField()

    def __str__(self):
        return self.titre_paie


class Prime(models.Model):
    titre_prime = models.CharField(max_length=255)
    description = models.TextField()
    montant = models.FloatField()
    paie = models.ForeignKey(Paie, related_name='primes', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titre_prime