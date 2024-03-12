from rest_framework import serializers
from . import paie_utils
from .models import Paie, Prime, Cotisation, DemandeSft


class PaieSerializer(serializers.HyperlinkedModelSerializer):
    # salaire_brut = serializers.IntegerField(read_only=True)
    # salaire_net = serializers.IntegerField(read_only=True)

    class Meta:
        model = Paie
        fields = ['url', 'id', 'titre_paie', 'date_remboursement', 'salaire_base', 'salaire_mois', 'salaire_annee', 'salaire_brut', 'salaire_net', 'primes', 'cotisations', 'agent']


class PrimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prime
        fields = ['url', 'id', 'titre_prime', 'description', 'montant', 'paies']


class CotisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cotisation
        fields = ['url', 'id', 'type_cotisation', 'taux', 'paies']


class DemandeSftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DemandeSft
        fields = ['url','id', 'nom_enfant', 'status', 'date_naissance_enfant', 'date_debut', 'date_fin', 'date_demande', 'membre_reversion']

