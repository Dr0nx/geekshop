# import os.path
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id_category=None, page=1):
    context = {
        'title': 'Geekshop | Каталог',
    }

    if id_category:
        prods = Product.objects.filter(category_id=id_category)
    else:
        prods = Product.objects.all()

    paginator = Paginator(prods, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    context['categories'] = ProductCategory.objects.all()

    #    with open("mainapp/fixtures/products.json", "w") as write_file:
    #        json.dump(context, write_file)
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'

    # context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        context['categories'] = ProductCategory.objects.all()
        return context
