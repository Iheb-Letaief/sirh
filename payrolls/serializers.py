from rest_framework import serializers
from . import paie_utils
from .models import Paie, Prime

class PaieSerializer(serializers.HyperlinkedModelSerializer):
    salaire_base = serializers.SerializerMethodField()
    salaire_brut = serializers.SerializerMethodField()
    salaire_net = serializers.SerializerMethodField()

    class Meta:
        model = Paie
        fields = ['url', 'id', 'titre_paie', 'date_remboursement', 'salaire_base', 'salaire_mois', 'salaire_annee', 'salaire_brut', 'salaire_net', 'primes', 'agent']

    def get_salaire_base(self, paie):
        agent = paie.agent
        return paie_utils.calcul_salaire_base(agent)
    def get_salaire_brut(self, paie):
        agent = paie.agent
        return paie_utils.calcul_salaire_brut(agent, paie)
    def get_salaire_net(self, paie):
        agent = paie.agent
        return paie_utils.calcul_salaire_net(agent, paie)


class PrimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prime
        fields = ['url', 'id', 'titre_prime', 'description', 'montant', 'paie']
