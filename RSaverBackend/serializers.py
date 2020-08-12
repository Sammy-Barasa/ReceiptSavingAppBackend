from django.contrib.auth.models import User
from .models import Receipt

from rest_framework import serializers

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        write_only_fields = ['password',]
        

    def create(self,validated_data):
        user = User(
        username=validated_data['username'], 
        email=validated_data['email'], 
        password=validated_data['password'])
        user.groups.none
        user.save()
        print('----------__')
        return user

            
# No need for HyperlinkedModelSerializer since user serializer does not depend on any relationship yet
'''
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
'''
