from . import views
from django.urls import path, include


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    # path('catalog/all/', views.catalog, name='catalog')
]