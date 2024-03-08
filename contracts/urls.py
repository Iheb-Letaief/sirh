from django.urls import path, include
from rest_framework import routers

from contracts import views

router = routers.DefaultRouter()
router.register(r'contrats', views.ContratViewSet, basename='contrat')


urlpatterns = [
path('', include(router.urls))
]