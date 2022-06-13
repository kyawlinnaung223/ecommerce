from django.urls import path
from .import views

urlpatterns=[
    path('',views.storepage,name="storepage"),
    path('cart/',views.cartpageview,name="cartpage"),
    path('checkout/',views.checkoutpageview,name="checkoutpage"),
]