from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='main'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/product-create', ProductCreateView.as_view(), name='product_create'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='product_update')
]
