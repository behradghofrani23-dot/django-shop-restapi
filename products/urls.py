from django.urls import include, path
from products import views
urlpatterns=[
    path("",views.shop,name="shop"),
    path("<slug:item>/",views.product,name="product"),
]