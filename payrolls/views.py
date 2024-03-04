from django.shortcuts import render
from rest_framework import viewsets

from payrolls.models import Paie

from payrolls.serializers import PaieSerializer

from payrolls.models import Prime

from payrolls.serializers import PrimeSerializer


# Create your views here.


# Paie views
class PaieViewSet(viewsets.ModelViewSet):
    queryset = Paie.objects.all()
    serializer_class = PaieSerializer

class PrimeViewSet(viewsets.ModelViewSet):
    queryset = Prime.objects.all()
    serializer_class = PrimeSerializer

