from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


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
