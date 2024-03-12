from rest_framework import routers
from django.urls import path, include

from payrolls import views

router = routers.DefaultRouter()
router.register(r'paies', views.PaieViewSet, basename='paie')
router.register(r'primes', views.PrimeViewSet, basename='prime')
router.register(r'demandeSft', views.DemandeSftViewSet)
router.register(r'cotisations', views.CotisationViewSet, basename='cotisation')




urlpatterns = [
path('', include(router.urls))
]