from django.http import Http404, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from . models import *
from cart.forms import CartAddProductForm
from django.core.mail import send_mail
from django.conf import settings

def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        'goods': goods,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    if request.method == 'POST':
        send_mail('Здравствуйте',
                  'Я хочу купить вашу недвижимость',
                  'django@gmail.com',
                  ['slang6682@gmail.com'])
    product = Products.objects.get(slug=product_slug)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
    }

    return render(request, 'goods/product.html', {'product': product, 'cart_product_form': cart_product_form})
