from django.db import models


class BlogPost(models.Model):
    """
    заголовок,
    slug (реализовать через CharField),
    содержимое,
    превью (изображение),
    дата создания,
    признак публикации,
    количество просмотров.
    """
    title = models.CharField(max_length=100, verbose_name='Название статьи')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слаг')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='media/blog_img/', verbose_name='Превью', null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Статус публикации')
    views_count = models.IntegerField(verbose_name='Количество просмотров')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'запись в блоге'
        verbose_name_plural = 'записи в блоге'
