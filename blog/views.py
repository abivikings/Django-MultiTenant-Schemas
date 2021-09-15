from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Posts
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        serializer = PostSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Post Created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)