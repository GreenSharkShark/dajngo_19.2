from django.shortcuts import render
from catalog.models import Product


def main_page(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/main_page.html', context)


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

