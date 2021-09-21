from coreschema.formats import validate_email
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from .models import Profile


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'