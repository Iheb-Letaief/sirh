from django.db import models
from employees.models import Agent

from payrolls import paie_utils


# Create your models here.

class Paie(models.Model):
    agent = models.ForeignKey(Agent, related_name='paies', on_delete=models.CASCADE, null=True, blank=True)
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
            ValueError("Il sagis'agit d'une paie negative")
            return 0
        return s

    @salaire_net.setter
    def salaire_net(self, value):
        self._salaire_net = value

    @property
    def salaire_mois(self):
        return self.salaire_net * 4
    @property
    def salaire_annee(self):
        return self.salaire_mois * 12

    def is_negative(self):
        return self.salaire_net < 0
    def regulariser_paie_negative(self):
        if self.is_negative():
            self.salaire_net(0)
            self.save(update_fields=['salaire_net'])




class Prime(models.Model):
    titre_prime = models.CharField(max_length=255)
    description = models.TextField()
    montant = models.FloatField()
    paie = models.ForeignKey(Paie, related_name='primes', on_delete=models.CASCADE, null=True, blank=True)
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
    paie = models.ForeignKey(Paie, related_name='indemnites', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titre_indemnite