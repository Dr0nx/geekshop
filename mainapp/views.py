from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, TemplateView, ListView

from mainapp.models import ProductCategory, Product


class IndexTemplateView(TemplateView):
    template_name = 'mainapp/index.html'
    context = {'title': 'Geekshop'}


class ProductList(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    context = {'title': 'Geekshop | Каталог'}

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)

        if self.kwargs.get('id_category'):
            prods = Product.objects.filter(category_id=self.kwargs['id_category'])
        else:
            prods = Product.objects.all()

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
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['products'] = product
        context['categories'] = ProductCategory.objects.all()
        return context
