
from django.db import models


class Contrat(models.Model):
    titre_contrat = models.CharField(max_length=255)
    type_contrat = models.CharField(max_length=255)
    description = models.TextField()
    duree = models.IntegerField(default=0)

    def __str__(self):
        return self.titre_contrat


class Agent(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True)
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
    conges_maladie = models.IntegerField(default=0)
    conges_payes = models.IntegerField(default=0)
    # droit_RIFSEEP = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"{self.nom} {self.prenom}"
        # self.droit_RIFSEEP = self.poste.droit_IFSE and self.poste.droit_CIA
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


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
