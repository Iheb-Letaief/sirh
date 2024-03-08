from django.shortcuts import render
from rest_framework import viewsets

from employees.models import Agent, Poste, Apprenti
from employees.serializers import AgentSerializer, PosteSerializer, ApprentiSerializer



# Agent views
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# Poste views
class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer

# Apprenti views
class ApprentiViewSet(viewsets.ModelViewSet):
    queryset = Apprenti.objects.all()
    serializer_class = ApprentiSerializer