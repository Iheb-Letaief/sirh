from rest_framework import serializers
from .models import Contrat


class ContratSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrat
        fields = ['url', 'id', 'titre_contrat', 'type_contrat', 'description', 'duree', 'nb_heures', 'date_debut', 'agents']
