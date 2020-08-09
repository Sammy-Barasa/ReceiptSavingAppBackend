from django.contrib.auth.models import User
from .models import Receipt

from rest_framework import serializers

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class meta:
        model=User
        field=['username','email','password']