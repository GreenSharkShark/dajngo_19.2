from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from catalog.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/main_page.html'
    my_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.my_context)
        return context


class CatalogPageView(TemplateView):
    template_name = 'catalog/catalog.html'
    extra_context = {'title': 'Каталог'}


class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты'}
