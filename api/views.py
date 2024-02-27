from django.shortcuts import render
from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Agent, Poste, Paie
from .serializers import AgentSerializer, PosteSerializer, PaieSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'agents': reverse('agent', request=request, format=format),
        'postes': reverse('poste', request=request, format=format),
        'paies' : reverse('paie', request=request, format=format)
    })

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer

    def get_queryset(self):
        queryset = Poste.objects.all()
        return queryset

class PaieViewSet(viewsets.ModelViewSet):
    queryset = Paie.objects.all()
    serializer_class = PaieSerializer










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



