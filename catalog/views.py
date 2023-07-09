from django.shortcuts import render


def main_page(request):
    return render(request, 'catalog/main_page.html')


def contacts_page(request):
    return render(request, 'catalog/contacts.html')

