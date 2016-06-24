from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    productlist = Product.objects.all()
    paginator = Paginator(productlist, 20)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    context = {
        'products': products
    }
    return render(request, 'shop/products.html', context)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    prices = product.price_set.all()
    context = {
        'product': product,
        'prices': prices
    }
    return render(request, 'shop/detail.html', context)
