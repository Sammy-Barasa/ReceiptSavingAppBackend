from django.contrib.auth.models import User
from .models import Receipt

from rest_framework import serializers

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=[
                'url',
                'id',
                'username',
                'first_name',
                'last_name',
                'email',
                ]

        def create(self,validated_data):
            return User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
            )