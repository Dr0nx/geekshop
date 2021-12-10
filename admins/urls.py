from django.urls import path

from admins.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, CategoryListView, \
    CategoryCreateView, CategoryDeleteView, CategoryUpdateView, IndexTemplateView, ProductListView, ProductCreateView, \
    ProductDeleteView, ProductUpdateView

app_name = 'admins'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),

    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_delete'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),

    path('product/', ProductListView.as_view(), name='admin_product'),
    path('product/create/', ProductCreateView.as_view(), name='admin_product_create'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_product_delete'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_product_update'),
]
