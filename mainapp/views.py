# import os.path
from django.shortcuts import render
from mainapp.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }

#    with open("mainapp/fixtures/products.json", "w") as write_file:
#        json.dump(context, write_file)

    return render(request, 'mainapp/products.html', context)
