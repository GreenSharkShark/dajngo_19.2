from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='main_page'),
    path('contacts/', ContactsPageView.as_view(), name='contacts_page'),
    path('catalog/', CatalogPageView.as_view(), name='catalog_page')
]
