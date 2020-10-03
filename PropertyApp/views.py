from django.shortcuts import render
from PropertyApp.models import Property
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from PropertyApp.permissions import IsOwnerOrReadOnly
from PropertyApp.serializers import UserSerializer, PropertySerializer
from rest_framework.response import Response

#from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

class PropertyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    
    Additionally, also provides an extra 'full address' display. 
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action (detail = True)
    def address (self, request, *args, **kwargs):
        the_property = self.get_object()
        return HttpResponse(the_property.address_text) #render complete address text as a html page

    def perform_create(self, serializer):
        serializer.save(agent = self.request.user)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides 'list' and 'detail' view for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
