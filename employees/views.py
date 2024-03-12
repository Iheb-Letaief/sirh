from django.shortcuts import render
from django.urls import reverse
from rest_framework import viewsets

from employees.models import Agent, Poste, Assfam
from employees.serializers import AgentSerializer, PosteSerializer, AssfamSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Agent views
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

# Poste views
class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer

# Assfam views
class AssfamViewSet(viewsets.ModelViewSet):
    queryset = Assfam.objects.all()
    serializer_class = AssfamSerializer
