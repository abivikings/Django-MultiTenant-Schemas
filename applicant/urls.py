from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .views import *
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'profile', ApplicantProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]