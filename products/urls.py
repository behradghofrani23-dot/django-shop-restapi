from django.urls import path
from .views import ProductListAPIView,ProductAPIView


urlpatterns = [
    path("all/", ProductListAPIView.as_view(), name="product-list"),
    path('<id:int>/', ProductAPIView.as_view(), name='product-item'),  
]