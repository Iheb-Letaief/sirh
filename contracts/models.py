from django.db import models

# Create your models here.
class Contrat(models.Model):
    titre_contrat = models.CharField(max_length=255)
    type_contrat = models.CharField(max_length=255)
    description = models.TextField()
    duree = models.IntegerField(default=0)

    def __str__(self):
        return self.titre_contrat