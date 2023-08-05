from django.db import models
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='Slug')
    content = models.TextField(verbose_name="Содержимое блога")
    image = models.ImageField(upload_to='blogs/', verbose_name='Превью')
    date_create = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    count_views = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.header)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.header.title()}'

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
