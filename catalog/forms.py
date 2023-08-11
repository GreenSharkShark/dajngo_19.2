from django import forms
from catalog.models import Product, Version

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'img')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'В названии продукта нельзя использовать слово: {cleaned_data}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'В описании продукта нельзя использовать слово: {cleaned_data}')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_published', 'description', 'category']
