from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='main'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('product-detail-view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/product-create', ProductCreateView.as_view(), name='product_create'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product-update-prohibited/', TemplateView.as_view(template_name='product_update_prohibited.html'), name='product_update_prohibited'),
]
