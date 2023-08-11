from django.db import models
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    Наименование,
    описание
    """
    category_name = models.CharField(max_length=100, verbose_name='Категория')
    category_description = models.TextField(verbose_name='Описание категории товара')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} {self.category_name} '

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    Наименование,
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
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')

    def __str__(self):
        return f'{self.pk} {self.name}, Категория: {self.category}, Цена: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    """
    Продукт,
    номер версии,
    название версии,
    признак текущей версии.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Версия продукта')
    number = models.IntegerField(verbose_name='Номер версии')
    name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Статус версии')

    def __str__(self):
        return f'{self.product} {self.name} {self.number} {self.is_active}'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продукта'
