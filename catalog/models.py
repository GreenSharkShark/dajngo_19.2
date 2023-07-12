from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    наименование,
    описание.
    """
    category_name = models.CharField(max_length=100, verbose_name='Категория')
    category_description = models.TextField(verbose_name='Описание категории товара')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.category_name} '

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    наименование,
    описание,
    изображение (превью),
    категория,
    цена за покупку,
    дата создания,
    дата последнего изменения.
    """
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='product_img/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_change_date = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')

    def __str__(self):
        return f'{self.id} {self.name}, Категория: {self.category}, Цена: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
