from django.shortcuts import render
from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Agent, Poste, Paie, Prime, Contrat, Declaration
from .serializers import AgentSerializer, PosteSerializer, PaieSerializer, PrimeSerializer, ContratSerializer, DeclarationSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'agents': reverse('agent', request=request, format=format),
        'postes': reverse('poste', request=request, format=format),
        'paies' : reverse('paie', request=request, format=format),
        'primes' : reverse('peimer', request=request, format=format),
        'contrats' : reverse('contrat', request=request, format=format),
        'declarations' : reverse('declaration', request=request, format=format)
    })


# Agent views
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


# Poste views
class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer


# Paie views
class PaieViewSet(viewsets.ModelViewSet):
    queryset = Paie.objects.all()
    serializer_class = PaieSerializer


class PrimeViewSet(viewsets.ModelViewSet):
    queryset = Prime.objects.all()
    serializer_class = PrimeSerializer


class ContratViewSet(viewsets.ModelViewSet):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer


class DeclarationViewSet(viewsets.ModelViewSet):
    queryset = Declaration.objects.all()
    serializer_class = DeclarationSerializer















"""
class AgentList(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AgentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class PosteList(generics.ListCreateAPIView):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer

class PosteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer
"""



