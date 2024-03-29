from django.urls import path, include
from rest_framework import routers

from employees import views

router = routers.DefaultRouter()
router.register(r'agents', views.AgentViewSet, basename='agent')
router.register(r'postes', views.PosteViewSet, basename='poste')
router.register(r'assfams', views.AssfamViewSet, basename='assfam')



urlpatterns = [
path('', include(router.urls))
]