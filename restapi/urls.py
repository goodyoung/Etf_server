from django.urls import path, include
from rest_framework import routers
from .views import  Main

# router = routers.DefaultRouter()
# router.register('',EtfDetailViewSet, basename='MyRestApi')
urlpatterns = [
    # path('',include(router.urls)),
    path('test/', Main, name='test'),
]
