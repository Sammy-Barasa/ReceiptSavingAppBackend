from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from django.http import Http404
from .serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# User Auth Endpoint

class AuthUserAPIView(CreateAPIView):
    serializer=UserSerializer
    # get user
    def get_user_object(self,pk,email):
        try:
            return User.objects.get(pk) or User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404
    
    
    def add_user(self,request):
        # add new user
        if request.method=="POST":
            user_data=request.user_data
            new_user=User(email=user_data.email,username=user_data.username,password=user_data.password)
            new_user.save()
            return Response(data="New user added succesfully",status=200)

    def auth_user(self,request):
        if request.method=="POST":
            data=request.data
            user=self.get_user_object(data.pk,data.email)
            if user:
                authenticated_user=authenticate(username=data.username,password=data.password,email=data.email)
                if authenticated_user is None:
                    return Response(data="Wrong email or password",status=401)
                return Response(data=authenticated_user,status=200)
            return Response(data="no such user",status=404)

            
            



# Image Submitting Endpoint

# User Receipt images Endpoint

# User Receipt pdf Endpoint