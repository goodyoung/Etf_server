from django.urls import path, include
from rest_framework import routers
from .serializer import EtfDetailsSerializer
from .views import EtfDetailViewSet
router = routers.DefaultRouter()
router.register('',EtfDetailViewSet, basename='MyRestApi')
urlpatterns = [
    path('',include(router.urls)),
    # path('',EtfDetailsSerializer , 'Etf'),
]
