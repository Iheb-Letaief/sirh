from rest_framework import routers
from django.urls import path, include

from api import views as api_views
from employees import views as employees_views
from payrolls import views as payrolls_views
from contracts import views as contracts_views


router = routers.DefaultRouter()
router.register(r'agents', employees_views.AgentViewSet, basename='agent')
router.register(r'postes', employees_views.PosteViewSet, basename='poste')
router.register(r'paies', payrolls_views.PaieViewSet, basename='paie')
router.register(r'primes', payrolls_views.PrimeViewSet, basename='prime')
router.register(r'contrats', contracts_views.ContratViewSet, basename='contrat')
router.register(r'declarations', api_views.DeclarationViewSet, basename='declaration')


urlpatterns = [
path('', include(router.urls))
]