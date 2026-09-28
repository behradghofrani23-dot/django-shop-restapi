from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer
class ProductListAPIView(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data,status=200)
class ProductAPIView(APIView):
    def get(self,request,slug):
        product=Product.objects.get(slug=slug)
        serializer=ProductSerializer(product)
        return Response(serializer.data,status=True)