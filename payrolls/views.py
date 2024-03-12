from django.shortcuts import render
from rest_framework import viewsets

from payrolls.models import Paie, Prime, Cotisation, DemandeSft

from payrolls.serializers import PaieSerializer, PrimeSerializer, CotisationSerializer, DemandeSftSerializer




# Create your views here.


# Paie views
class PaieViewSet(viewsets.ModelViewSet):
    queryset = Paie.objects.all()
    serializer_class = PaieSerializer

class PrimeViewSet(viewsets.ModelViewSet):
    queryset = Prime.objects.all()
    serializer_class = PrimeSerializer

class CotisationViewSet(viewsets.ModelViewSet):
    queryset = Cotisation.objects.all()
    serializer_class = CotisationSerializer

class DemandeSftViewSet(viewsets.ModelViewSet):
    queryset = DemandeSft.objects.all()
    serializer_class = DemandeSftSerializer

