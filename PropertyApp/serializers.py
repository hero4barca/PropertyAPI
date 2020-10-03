from rest_framework import serializers
from PropertyApp.models import *
from django.contrib.auth.models import User


class PropertySerializer(serializers.HyperlinkedModelSerializer):

    agent = serializers.ReadOnlyField(source = 'agent.username')
    address = serializers.HyperlinkedIdentityField(view_name = 'property-address')
    class Meta:
        model = Property
        fields = ['url', 'id', 'description', 'street_address', 
                    'address_line_2', 'postcode', 'city', 'agent','address']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    properties = serializers.HyperlinkedRelatedField(many=True, view_name = 'property-detail', read_only= True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'properties']


