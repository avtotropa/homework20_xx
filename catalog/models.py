from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Курс')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена курса')
    image = models.ImageField(upload_to='catalog/', verbose_name='Фотография', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
