from rest_framework import serializers
from .models import Agent, Poste, Apprenti

class PosteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poste
        fields = ['url', 'id', 'agent', 'titre_poste', 'description', 'droit_NBI', 'droit_ZUS', 'droit_IFSE', 'droit_CIA']


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = ['url','id', 'nom', 'prenom', 'username', 'email', 'statut', 'date_naissance', 'age', 'contrat', 'nationality', 'cin',
                  'date_embauche', 'nb_enfants', 'nb_heure', 'taux_cotisation', 'taux_impot', 'salaire_horaire', 'annees_apprentissage', 'salaire_apprenti', 'postes', 'created_at', 'modified_at']

class ApprentiSerializer(AgentSerializer):
    # annees_apprentissage = serializers.ReadOnlyField()
    # salaire_apprenti = serializers.ReadOnlyField()

    class Meta:
        model = Apprenti
        fields = ['url','id', 'agent', 'salaire_apprenti', 'annees_apprentissage']


