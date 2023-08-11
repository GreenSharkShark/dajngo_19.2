from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Moderator').exists():
            return ['name', 'price', 'date_of_creation', 'last_change_date', 'creator']
        return []
