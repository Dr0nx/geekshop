from django.contrib.auth.decorators import user_passes_test

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from admins.forms import UserAdminRegisterForm, ProductCategoryAdminForm, ProductAdminForm, UserAdminProfileForm, \
    ProductUpdate
from authapp.models import User
from mainapp.models import ProductCategory, Product


class IndexTemplateView(TemplateView):
    template_name = 'admins/admin.html'


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создать пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Изменение пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    success_url = reverse_lazy('admins:admin_category')
    form_class = ProductCategoryAdminForm


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = ProductCategoryAdminForm
    success_url = reverse_lazy('admins:admin_category')


class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin-product-read.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'admins/admin-product-create.html'
    success_url = reverse_lazy('admins:admin_product')
    form_class = ProductUpdate


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    success_url = reverse_lazy('admins:admin_product')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductAdminForm
    success_url = reverse_lazy('admins:admin_product')
