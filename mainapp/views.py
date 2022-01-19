
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.cache import cache
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache
from django.views.generic import DetailView, TemplateView, ListView

from mainapp.models import ProductCategory, Product


def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return ProductCategory.objects.all()


def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key, product)
        return product
    else:
        return Product.objects.get(id=pk)


class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'
    context = {'title': 'Geekshop'}


# @method_decorator([never_cache], name='dispatch')
# @method_decorator([cache_page(3600)], name='dispatch')
class ProductList(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    context = {'title': 'Geekshop | Каталог'}

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)

        if self.kwargs.get('id_category'):
           prods = Product.objects.filter(category_id=self.kwargs['id_category']).select_related('category')
        else:
           prods = Product.objects.all().select_related('category')

        # prods = get_link_product()

        page = self.kwargs.get('page')
        paginator = Paginator(prods, per_page=3)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context['products'] = products_paginator
        context['categories'] = ProductCategory.objects.all()
        # context['categories'] = get_link_category()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        # context['product'] = get_product(self.kwargs.get('pk'))
        # context['categories'] = ProductCategory.objects.all()
        return context
