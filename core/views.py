from django.shortcuts import render
from products.models import Product


def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
        'trending_products': products[:4],
        
    }

    return render(request, 'index.html', context)