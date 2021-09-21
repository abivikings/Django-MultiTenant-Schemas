from rest_framework_simplejwt.tokens import RefreshToken
from rest_auth.views import LoginView as RestLoginView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ApplicantSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Profile


class ApplicantProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplicantSerializer
    queryset = Profile.objects.all()

