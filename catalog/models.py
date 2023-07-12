from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    наименование,
    описание.
    """
    category_name = models.CharField(max_length=100, verbose_name='Категория')
    category_description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category_name}'


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
