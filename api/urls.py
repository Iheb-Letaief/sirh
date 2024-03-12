from rest_framework import routers
from django.urls import path, include

from api import views as api_views
from employees import views as employees_views
from payrolls import views as payrolls_views
from contracts import views as contracts_views


router = routers.DefaultRouter()
# router.register(r'agents', employees_views.AgentViewSet, basename='agent')
# router.register(r'postes', employees_views.PosteViewSet, basename='poste')
# router.register(r'paies', payrolls_views.PaieViewSet, basename='paie')
# router.register(r'primes', payrolls_views.PrimeViewSet, basename='prime')
# router.register(r'contrats', contracts_views.ContratViewSet, basename='contrat')

router.register(r'declarations', api_views.DeclarationViewSet, basename='declaration')

employees_router = routers.DefaultRouter()
employees_router.register(r'agents', employees_views.AgentViewSet)
employees_router.register(r'postes', employees_views.PosteViewSet)

payrolls_router = routers.DefaultRouter()
payrolls_router.register(r'paies', payrolls_views.PaieViewSet)
payrolls_router.register(r'primes', payrolls_views.PrimeViewSet)
payrolls_router.register(r'cotisations', payrolls_views.CotisationViewSet)
payrolls_router.register(r'demandeSft', payrolls_views.DemandeSftViewSet)

contracts_router = routers.DefaultRouter()
contracts_router.register(r'contrats', contracts_views.ContratViewSet)

urlpatterns = [
path('', include(router.urls)),
path('employees/', include(employees_router.urls)),
path('payrolls/', include(payrolls_router.urls)),
path('contracts/', include(contracts_router.urls)),

]