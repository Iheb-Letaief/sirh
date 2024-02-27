import uuid

from django.db import models


class Agent(models.Model):
    #user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    #photo = models.ImageField(upload_to='images/', blank=True, null=True)
    date_naissance = models.DateField()
    statut = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    cin = models.CharField(max_length=255)
    date_embauche = models.DateField()
    nb_enfants = models.IntegerField(default=0)
    nb_heure = models.IntegerField(default=0)
    #droit_RIFSEEP = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"{self.nom} {self.prenom}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Poste(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    agent = models.ForeignKey(Agent, related_name='postes', on_delete=models.CASCADE, null=True, blank=True)
    titre_poste = models.CharField(max_length=255)
    description = models.TextField()
    droit_NBI = models.BooleanField(default=False)
    droit_ZUS = models.BooleanField(default=False)
    droit_IFSE = models.BooleanField(default=False)
    droit_CIA = models.BooleanField(default=False)

    def __str__(self):
        return self.titre_poste

class Paie(models.Model):
    agents = models.ManyToManyField(Agent)
    titre_paie = models.CharField(max_length=255)
    date_remboursement = models.DateTimeField(auto_now_add=True)
    salaire_mois = models.FloatField()
    salaire_annee = models.FloatField()
    salaire_brute = models.FloatField()
    salaire_net = models.FloatField()

    def __str__(self):
        return self.titre_paie
