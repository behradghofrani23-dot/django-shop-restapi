from django.urls import path
from .views import ProductListAPIView,ProductAPIView,ProductTaChand


urlpatterns = [
    path("all/", ProductListAPIView.as_view(), name="product-list"),
    path('<slug:slug>/', ProductAPIView.as_view(), name='product-item'),
    path("<int:id>",ProductTaChand.as_view(),name="product-ta-chand") 
]