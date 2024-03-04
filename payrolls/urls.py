from rest_framework import routers
from django.urls import path, include

from payrolls import views

router = routers.DefaultRouter()
router.register(r'paies', views.PaieViewSet, basename='paie')
router.register(r'primes', views.PrimeViewSet, basename='prime')



urlpatterns = [
path('', include(router.urls))
]