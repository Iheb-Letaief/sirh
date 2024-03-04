from .models import  Declaration
from rest_framework import serializers


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
