from django.shortcuts import render
from products.models import Product


def index(request):
    products = Product.objects.all().order_by('-created_at')

    context = {
        'products': products,
        'trending_products': products[:4],
        'top_products': products.order_by('-count')[:6],
    }

    return render(request, 'index.html', context)