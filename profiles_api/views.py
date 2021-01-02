from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
from profiles_api import models


class HelloApiView(APIView):
    '''Test API View'''

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView features'''

        an_apiview = [
            'Uses HTTP methods as function (GET, POST, PATCH, PUT, DELETE)',
            'Is similar to traditional Django VIew',
            'Give you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        return Response({'message': f'Hello {name}'})

    def put(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Handle a partial update of an object'''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        '''Delete a object'''
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test viewset API'''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''Return a hello message'''
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        '''Create a hello message with your name'''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        return Response({'message': f'Hello {name}'})

    def retrieve(self, request, pk=None):
        '''Handle getting an object by it ids'''
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        '''Handle updating part of an object'''
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        '''Handle removing an object'''
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating user account'''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfiles.objects.all()
