from rest_framework import routers
from django.urls import path, include

from api import views


router = routers.DefaultRouter()
router.register(r'agents', views.AgentViewSet, basename='agent')
router.register(r'postes', views.PosteViewSet, basename='poste')
router.register(r'paies', views.PaieViewSet, basename='paie')
router.register(r'primes', views.PrimeViewSet, basename='prime')
router.register(r'contrats', views.ContratViewSet, basename='contrat')
router.register(r'declarations', views.DeclarationViewSet, basename='declaration')


urlpatterns = [
path('', include(router.urls))
]