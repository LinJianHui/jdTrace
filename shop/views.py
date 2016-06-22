from django.shortcuts import render
from .models import Product, Price
# Create your views here.


def index(request):
    return render(request, 'shop/products.html', {'message': 'hello'})


def detail(request, product_id):
    return render(request, 'shop/detail.html', {'message': 'hello'})
