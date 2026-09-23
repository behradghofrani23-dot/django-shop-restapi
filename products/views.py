from django.shortcuts import render
from .models import Product
# Create your views here.
def shop(request):
    b=Product.objects.all()
    return render(request,"shop.html",{"products":b})