from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class DispatchMixin:
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.creator != self.request.user:
            return HttpResponseForbidden(
                "У вас нет прав на редактирование или удаление продукта, создателем которого вы не являетесь."
            )
        return super().dispatch(request, *args, **kwargs)


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/main.html'
    my_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.my_context)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.creator = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, DispatchMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:main')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DispatchMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:main')


class CatalogView(TemplateView):
    template_name = 'catalog/catalog.html'
    extra_context = {'title': 'Каталог'}


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты'}
