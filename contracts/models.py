import datetime

from django.db import models
from datetime import date

# Create your models here.
class Contrat(models.Model):

    # types = (
    #     ('CDD', 'CDD'),
    #     ('CDI', 'CDI'),
    #     ('Stage', 'Stage'),
    #     ('Apprentissage', 'Apprentissage'),
    #     #('Interim', 'Interim'),
    # )

    types = {
        "Classique": {
            "CDD": "CDD",
            "CDI": "CDI",
        },
        "Spécifique": {
            "Urgent": "Urgent",
            "Stage": "Stage",
            "Apprentissage": "Apprentissage",
        }


    }

    titre_contrat = models.CharField(max_length=255)
    type_contrat = models.CharField(choices=types, max_length=255, default='CDI')
    description = models.TextField()
    duree = models.IntegerField(default=0)
    nb_heures = models.IntegerField(default=0)
    date_debut = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.titre_contrat

