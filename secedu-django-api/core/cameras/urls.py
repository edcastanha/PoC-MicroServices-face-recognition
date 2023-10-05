from django.urls import include, path
from rest_framework import routers
from core.cameras.api import NotaFiscalViewSet, CamerasViewSet, LocaisViewSet, FrequenciasViewSet, TarefasViewSet

# URLs DE API
router = routers.DefaultRouter()
router.register(r'notasfiscais', NotaFiscalViewSet, basename='notasfiscais')
router.register(r'cameras', CamerasViewSet, basename='cameras')
router.register(r'locais', LocaisViewSet, basename='locais')
router.register(r'frequencias', FrequenciasViewSet, basename='frequencias')
router.register(r'tarefas', TarefasViewSet, basename='tarefas')

urlpatterns = [
    path('', include(router.urls)), #API REST
]