from rest_framework import routers
from django.urls import path, include

from api import views


router = routers.DefaultRouter()
router.register(r'agents', views.AgentViewSet, basename='agent')
router.register(r'postes', views.PosteViewSet, basename='poste')
router.register(r'paies', views.PaieViewSet, basename='paie')


urlpatterns = [
path('', include(router.urls))
]