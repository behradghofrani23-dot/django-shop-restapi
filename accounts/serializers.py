from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
class aasdasd(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields="__all__"
    def create(self, validated_data):
        user=CustomUser.objects.create_user(**self.validated_data)
        
        return user 
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    def validate(self, attrs):
        
        user=authenticate(username=username,password=password)
        if user is None:
            raise serializers.ValidationError("you have entered something wrong")
        if not user.is_active:
            raise serializers.ValidationError("the user is not active")
        refresh =RefreshToken.for_user(user)
        attrs["user"]=user
        attrs["refresh"]=str(refresh)
        attrs["access"]=str(refresh.acces_token)
        return attrs 