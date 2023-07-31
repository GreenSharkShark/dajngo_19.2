from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DeleteView
from catalog.forms import ProductForm
from catalog.models import Product
from django.urls import reverse_lazy


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/main_page.html'
    my_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.my_context)
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:main')


class CatalogView(TemplateView):
    template_name = 'catalog/catalog.html'
    extra_context = {'title': 'Каталог'}


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты'}
