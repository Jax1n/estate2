from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from goods.models import Products
from .carts import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
  cart = Cart(request)
  product = get_object_or_404(Products, id=product_id)
  form = CartAddProductForm(request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    cart.add(product=product),
  return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
  cart = Cart(request)
  product = get_object_or_404(Products, id=product_id)
  cart.remove(product)
  return redirect('cart:cart_detail')

def cart_detail(request):
  cart = Cart(request)
  return render(request, 'detail.html', {'cart': cart})