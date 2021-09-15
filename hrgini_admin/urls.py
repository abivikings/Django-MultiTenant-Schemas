from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import *

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet)

urlpatterns = [
    path('registration/', OrganizationViewSetPublic, name='registration'),
    path('', include(router.urls)),
]