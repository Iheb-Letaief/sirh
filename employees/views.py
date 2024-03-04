from django.shortcuts import render
from rest_framework import viewsets

from employees.models import Agent
from employees.serializers import AgentSerializer
from employees.models import Poste
from employees.serializers import PosteSerializer


# Agent views
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# Poste views
class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer