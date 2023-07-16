from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main_page, contacts_page, catalog_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', main_page, name='main_page'),
    path('contacts/', contacts_page, name='contacts_page'),
    path('catalog/', catalog_page, name='catalog_page')
]
