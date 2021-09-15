from coreschema.formats import validate_email
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import serializers, exceptions
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=5, write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer, ModelBackend):
    email = serializers.EmailField(max_length=50, validators=[validate_email])
    password = serializers.CharField(
        min_length=5, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def authenticate(self, request, email=None, password=None, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not email or not password:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        credentials = {
            get_user_model().USERNAME_FIELD: email,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return user, None
