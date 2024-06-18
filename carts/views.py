from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

def cart(request):
    return render(request,'store/cart.html')

def _cart_id(request):  
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):  
    product = Product.objects.get(id=product_id)  
    print(product)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    print("hey")
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1 
        cart_item.save()
    except :
        cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart
            )
        cart_item.save()
    print("yes")
    return HttpResponse(cart_item.product)

          