from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .views import *
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginViewSet.as_view(), name='token_obtain_pair'),
]