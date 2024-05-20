from django.shortcuts import render, redirect
from django.views.generic import ListView
from goods.models import Categories
from goods.models import Products
from django.db.models import Q


# def search(request):
#     if request.method.method == 'GET':
#         search = request.GET.get('search')
#         post = Products.objects.all().filter(name=search)
#         return render(request, 'home.html', {'post': post})

# def search(request):
#     return render(request, 'home.html')


def index(request):
    categories = Categories.objects.all()
    products = Products.objects.filter(is_featured=True)
    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def cart(request):
    return redirect(request, 'cart/')

# def catalog(request):
#     return redirect(request, 'catalog/all/')