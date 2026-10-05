from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer, LoginSerializer
    
class SignupAPIView(APIView):

    def post(self, request):

        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            return Response(
                {
                    "message": "ثبت نام   انجام شد",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    }
                },
                status=201
            )

        return Response(serializer.errors, status=400)
class LoginApiView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {
                    "message":"login was successfully",
                    "access":serializer.validated_data['access'],
                    "refresh":serializer.validated_data['refresh'],
                    "user":{
                        "id":serializer.validated_data["user"].id,
                        "username":serializer.validated_data['user'].username,
                    }
                },
                status=200
            )
        return Response(serializer.errors,status=400)
        