from django.shortcuts import render
from rest_framework import viewsets
from contracts.models import Contrat
from contracts.serializers import ContratSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'contrats' : reverse('contrat', request=request, format=format),
    })

class ContratViewSet(viewsets.ModelViewSet):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer
