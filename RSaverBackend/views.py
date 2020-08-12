from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from django.http import Http404
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,permission_classes
from rest_framework.renderers import JSONRenderer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# User Auth Endpoint

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def auth_user(request):
    if request.method=="POST":
            data=request.data
            print(data)
            user=User.objects.get(email=data['email'])
            print(user)
            
            print('--------')
            if user:
                authenticated_user=authenticate(username=data["username"],password=data["password"],email=data["email"])
                if authenticated_user is None:
                    return Response({"message":"Wrong email or password","status":401})
                serializer=UserSerializer(authenticated_user)
                json=JSONRenderer().render(serializer.data)
                print(json)
                return Response({'user':json,'status':200})
            return Response({"message":"no such user","status":404})
    return Response({'message':"hello world"})

# User Creating Endpoint

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def add_user(request):
    if request.method =="POST":
            new_user = request.data
            new_user_username = new_user['username']
            print(new_user)
            serializer=UserSerializer(data=new_user)
            print('--------------------------------')
            print(serializer.get_fields())
            print('--------------------------------')
            valid=serializer.is_valid()
            print(serializer.validated_data)
            json=JSONRenderer().render(serializer.data)
            print(json)
            if valid:
                return Response({'messagee':'new user,{new_user_username} added','status':200})
            return Response({"message":"user not added","status":404})
    return Response({'message':"Add a new user"})



# class AuthUserAPIView(CreateAPIView):
    
#     queryset = User.objects.all()
#     serializer_class = UserSerializer(queryset)
#     permission_classes = [AllowAny]
  

    # get user
    # def get_user_object(self,pk,email):
    #     try:
    #         return User.objects.get(pk) or User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         raise Http404
    
    
    # def add_user(self,request):
    #     # add new user
    #     if request.method=="POST":
    #         user_data=request.user_data
    #         new_user=User(email=user_data.email,username=user_data.username,password=user_data.password)
    #         new_user.save()
    #         return Response(data="New user added succesfully",status=200)

  

#     {
# "email": "kesammybarasa@gmail.com", 
# "username":"barasa",
# "password": "barasa"
# }   
#    {
# "email": "test1@gmail.com", 
# "username":"test1",
# "password": "test1"
# }         



# Image Submitting Endpoint

# User Receipt images Endpoint

# User Receipt pdf Endpoint