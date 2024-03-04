from rest_framework import serializers
from .models import Agent, Poste

class PosteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poste
        fields = ['url', 'id', 'agent', 'titre_poste', 'description', 'droit_NBI', 'droit_ZUS', 'droit_IFSE', 'droit_CIA']


class AgentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Agent
        fields = ['url','id', 'nom', 'prenom', 'email', 'statut', 'date_naissance', 'contrat', 'nationality', 'cin',
                  'date_embauche', 'nb_enfants', 'nb_heure', 'taux_cotisation', 'taux_impot', 'salaire_horaire', 'postes', 'created_at', 'modified_at']
