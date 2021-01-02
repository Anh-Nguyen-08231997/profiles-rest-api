from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    '''Serializes a name field for testing our APIView'''

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializes a user profile object'''

    class Meta:
        model = models.UserProfiles
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        '''Create and return a new user'''
        user = models.UserProfiles.objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            password=validated_data.get('password')
        )
        return user

    def update(self, instance, validated_data):
        '''Handle updating user account'''
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_dat)
