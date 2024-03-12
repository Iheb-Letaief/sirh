from django.db import models
from django.db.models import Sum
import datetime

from employees.models import Agent

from payrolls import paie_utils


# Create your models here.

class Paie(models.Model):
    agent = models.ForeignKey(Agent, related_name='paies', on_delete=models.SET_NULL, null=True, blank=True)
    titre_paie = models.CharField(max_length=255)
    date_remboursement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre_paie

    # def save(self, *args, **kwargs):
    #     if self.salaire_net < 0:
    #         self.salaire_net(0)
    #     super().save(*args, **kwargs)

    @property
    def salaire_base(self):
        agent = self.agent
        return paie_utils.calcul_salaire_base(agent)
    @property
    def salaire_brut(self):
        agent = self.agent
        return paie_utils.calcul_salaire_brut(agent, self)

    @property
    def salaire_net(self):
        agent = self.agent
        s = paie_utils.calcul_salaire_net(agent, self)
        if s < 0:
            ValueError("Il s'agit d'une paie negative")
            return 0
        return s

    @property
    def salaire_mois(self):
        return self.salaire_net * 4
    @property
    def salaire_annee(self):
        return self.salaire_mois * 12

    @property
    def taux_cotisation(self):
        total_cotisations = self.cotisations.all().aggregate(total=Sum('taux'))['total'] or 0
        return total_cotisations


class Prime(models.Model):
    titre_prime = models.CharField(max_length=255)
    description = models.TextField()
    montant = models.FloatField()
    paies = models.ManyToManyField(Paie, related_name='primes', null=True, blank=True)
    #prime_cherte_de_vie = models.BooleanField(default=False)

    def __str__(self):
        return self.titre_prime

    # def save(self, *args, **kwargs):
    #     if self.titre_prime == 'Cherté de vie':
    #         self.prime_cherte_de_vie = True
    #     super().save(*args, **kwargs)

class Indemnite(models.Model):
    titre_indemnite = models.CharField(max_length=255)
    description = models.TextField()
    montant = models.FloatField()
    paie = models.ForeignKey(Paie, related_name='indemnites', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre_indemnite

class Cotisation(models.Model):
    types = {
        "CSG": "CSG",
        "CRDS": "CRDS",
        "CSA": "CSA",
        "Cotisation Assurance maladie": "Cotisation Assurance maladie",
        "Cotisation chomage": "Cotisation chomage",
        "Cotisation retraite": "Cotisation retraite",
    }

    type_cotisation = models.CharField(choices=types, max_length=255, default='CSG')
    taux = models.FloatField()
    paies = models.ManyToManyField(Paie, related_name='cotisations', null=True, blank=True)

    def __str__(self):
        return self.type_cotisation


class DemandeSft(models.Model):
    statuses = {
        "En attente": "En attente",
        "Acceptée": "Acceptée",
        "Refusée": "Refusée",
    }

    nom_enfant = models.CharField(max_length=255)
    status = models.CharField(choices=statuses, max_length=255, default='En attente')
    date_naissance_enfant = models.DateField(null=True)
    date_demande = models.DateTimeField(auto_now_add=True, null=True)
    membre_reversion = models.ForeignKey(Agent, related_name='demandes_Sft', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre_demande

    @property
    def titre_demande(self):
        return f"Demande SFT pour {self.nom_enfant}"

    @property
    def date_debut(self):
        first_day_current_month = self.date_naissance_enfant.replace(day=1)

        first_day_next_month = first_day_current_month + datetime.timedelta(days=31)
        first_day_next_month = first_day_next_month.replace(day=1, year=self.date_demande.year)

        return first_day_next_month

    @property
    def date_fin(self):
        age_20_years = self.date_naissance_enfant.replace(year=self.date_naissance_enfant.year + 20)
        return age_20_years.replace(day=1)


