from django.shortcuts import render
from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import Declaration

from api.serializers import DeclarationSerializer

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'agents': reverse('agent', request=request, format=format),
#         'postes': reverse('poste', request=request, format=format),
#         'paies' : reverse('paie', request=request, format=format),
#         'primes' : reverse('prime', request=request, format=format),
#         'contrats' : reverse('contrat', request=request, format=format),
#         'declarations' : reverse('declaration', request=request, format=format)
#     })


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



