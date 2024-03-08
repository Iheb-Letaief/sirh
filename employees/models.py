from django.db import models
import datetime
import logging

from contracts.models import Contrat

from payrolls import paie_utils


# Create your models here.

class Agent(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    #username = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    # photo = models.ImageField(upload_to='images/', blank=True, null=True)

    date_naissance = models.DateField()
    statut = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    cin = models.CharField(max_length=255)
    date_embauche = models.DateField()

    contrat = models.ForeignKey(Contrat, related_name='agents', on_delete=models.CASCADE, null=True)
    nb_enfants = models.IntegerField(default=0)
    nb_heure = models.IntegerField(default=0)

    taux_cotisation = models.IntegerField(default=0)
    taux_impot = models.IntegerField(default=0)

    salaire_horaire = models.FloatField(default=0)
    is_apprenti = models.BooleanField(default=False)
    is_stagiaire = models.BooleanField(default=False)

    conges_maladie = models.IntegerField(default=0)
    conges_payes = models.IntegerField(default=0)
    conges_bonifies = models.IntegerField(default=0)

    # droit_RIFSEEP = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.username

    @property
    def username(self):
        return f"{self.nom} {self.prenom}"

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_naissance.year
    @property
    def annees_apprentissage(self):
        if self.contrat.type_contrat == 'Apprentissage':
            nb_annees = datetime.datetime.now().year - self.contrat.date_debut.year
            if nb_annees == 0:
                return 1
            else:
                ValueError("L'apprenti n'a pas le droit de travailler plus de 3 ans")
        return nb_annees

    @property
    def salaire_apprenti(self):
        if self.age in range(18, 27):
            if self.contrat.type_contrat == 'Apprentissage':
                pourcentage_smic = paie_utils.get_pourcentage_smic(self.age, self.annees_apprentissage)
                return pourcentage_smic * paie_utils.smic_mois
        else:
            ValueError("L'apprenti doit avoir entre 18 et 26 ans")


class Apprenti(models.Model):
    agent = models.OneToOneField(Agent, related_name='apprenti', on_delete=models.CASCADE, null=True, blank=True)



class Poste(models.Model):
    agent = models.ForeignKey(Agent, related_name='postes', on_delete=models.CASCADE, null=True, blank=True)
    titre_poste = models.CharField(max_length=255)
    description = models.TextField()
    droit_NBI = models.BooleanField(default=False)
    droit_ZUS = models.BooleanField(default=False)
    droit_IFSE = models.BooleanField(default=False)
    droit_CIA = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre_poste