from rest_framework import serializers
from .models import Organization, Domain, OrgTemp
from django.contrib.auth.models import User


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationPublicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrgTemp
        fields = '__all__'


class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'email']
