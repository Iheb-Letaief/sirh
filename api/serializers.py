from . import paie_utils
from .models import Agent, Poste, Paie, Contrat, Prime, Declaration
from rest_framework import serializers


class PosteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poste
        fields = ['url', 'id', 'agent', 'titre_poste', 'description', 'droit_NBI', 'droit_ZUS', 'droit_IFSE', 'droit_CIA']


class AgentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Agent
        fields = ['url','id', 'nom', 'prenom', 'email', 'statut', 'date_naissance', 'contrat', 'nationality', 'cin',
                  'date_embauche', 'nb_enfants', 'nb_heure', 'salaire_horaire', 'postes', 'created_at', 'modified_at']


class PaieSerializer(serializers.HyperlinkedModelSerializer):
    salaire_base = serializers.SerializerMethodField()
    salaire_brut = serializers.SerializerMethodField()

    class Meta:
        model = Paie
        fields = ['url', 'id', 'titre_paie', 'date_remboursement', 'salaire_base', 'salaire_mois', 'salaire_annee', 'salaire_brut', 'salaire_net', 'primes', 'agent']

    def get_salaire_base(self, paie):
        agent = paie.agent
        return paie_utils.calcul_salaire_base(agent)
    def get_salaire_brut(self, paie):
        agent = paie.agent
        return paie_utils.calcul_salaire_brut(agent, paie)

class PrimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prime
        fields = ['url', 'id', 'titre_prime', 'description', 'montant', 'paie']

class ContratSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrat
        fields = ['url', 'id', 'titre_contrat', 'type_contrat', 'duree', 'agents']


class DeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        fields = ['url', 'id', 'titre_declaration', 'type_declaration', 'pourcentage', 'montant', 'agent', 'paies']


"""
class AgentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='agent-detail')
    #postes = serializers.HyperlinkedRelatedField(many=True, view_name='poste-detail', read_only=True)

    class Meta:
        model = Agent
        fields = ('url', 'id', 'email', 'date_naissance', 'statut', 'nationality', 'cin',
                  'date_embauche', 'nb_enfants', 'nb_heure', 'created_at', 'modified_at')
        #extra_kwargs = {'url': {'view_name': 'agent-detail', 'lookup_field': 'id'}}

class PosteSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='poste-detail')
    agent = AgentSerializer(read_only=True)
    #agent_url = serializers.HyperlinkedRelatedField(view_name='agent-detail', lookup_field='agent_id')


    class Meta:
        model = Poste
        fields = ('url', 'id', 'agent', 'titre_poste', 'description', 'droit_NBI', 'droit_ZUS', 'droit_IFSE', 'droit_CIA')
        #extra_kwargs = {'url': {'view_name': 'poste-detail', 'lookup_field': 'id'}}

"""
