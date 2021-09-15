from django.contrib.auth.hashers import make_password
from django.db import connection
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import OrganizationSerializer, OrganizationPublicSerializer
from .models import Organization, Domain
from organization.models import Users


@api_view(['post'])
def OrganizationViewSetPublic(request):
    serializer_context = {
        'request': request,
    }
    serializer = OrganizationPublicSerializer(data=request.data, context=serializer_context)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'Data Submitted. Please Wait for admin approval.'})
    else:
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class OrganizationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }
        serializer = OrganizationSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.context["schema_name"] = request.data['short_name']
            tenant = serializer.save()
            domain = Domain()
            domain.domain = request.data['short_name'] + '.localhost'
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
            connection.set_schema(request.data['short_name'], True)
            User.objects.create(email=request.data['email'], password=make_password('12345'))
            connection.set_schema_to_public()
            return Response({'status': 'Organization Created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
