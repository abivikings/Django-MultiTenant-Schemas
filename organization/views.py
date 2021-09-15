from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Users
from .serializers import *
from rest_auth.views import LoginView as RestLoginView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

# views will goes to here

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginViewSet(RestLoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        if email is None:
            return Response({'error': 'Email not registered'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(email=email)
            if not user.check_password(request.data['password']):
                return Response({'error': 'Email or password incorrect'}, status=status.HTTP_400_BAD_REQUEST)
            token = get_tokens_for_user(user)
            return Response({"token": token, "user": UserSerializer(user,context={'request': request}).data},status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_403_FORBIDDEN)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            User.objects.create(username=request.data['username'], password=make_password(request.data['password']), email=request.data['email'], is_staff=True, is_active=True)
            return Response({'status': 'User Created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
