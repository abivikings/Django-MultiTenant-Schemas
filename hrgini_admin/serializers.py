from rest_framework import serializers
from .models import Organization, Domain, OrgTemp


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationPublicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrgTemp
        fields = '__all__'