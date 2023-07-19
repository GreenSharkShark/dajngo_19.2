from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/main_page.html'
    my_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.my_context)
        return context


def catalog_page(request):
    context = {
        'title': 'Каталог'
    }
    return render(request, 'catalog/catalog.html', context)


def contacts_page(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
