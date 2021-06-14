from django.shortcuts import render
from . import models
from django.http import HttpResponse
from math import ceil


# Create your views here.
def index(request):
    # return HttpResponse("krishna")
    # products = models.product.objects.all()
    # print(products)
    # n = len(products)
    # nslide = n // 4 + ceil((n / 4) + (n // 4))
    allprod = []
    catprod = models.product.objects.values('category', 'id')
    cats = {
        item['category'] for item in catprod
    }
    for cat in cats:
        prod = models.product.objects.filter(category=cat)
        n = len(prod)
        nslide = n // 4 + ceil((n / 4) + (n // 4))
        allprod.append([prod, range(1, nslide), nslide])
    # allprod = [
    #     [products, range(1, nslide), nslide],
    #     [products, range(1, nslide), nslide]
    # ]
    # prams = {
    #     'no_slides': nslide,
    #     'range': range(1, nslide),
    #     'product': products
    # }
    prams = {
        'allprod': allprod,
    }
    return render(request, 'shop/index.html', prams)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("about")


def track(request):
    return HttpResponse("about")


def service(request):
    return HttpResponse("about")


def productview(request):
    return HttpResponse("about")


def product(request):
    return HttpResponse("about")


def search(request):
    return HttpResponse("about")
