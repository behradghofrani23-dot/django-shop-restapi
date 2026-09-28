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
    def get(self,request,id):
        product=Product.objects.order_by("id")[:id]
        serializer=ProductSerializer(product)
        return Response(serializer.data,status=True)