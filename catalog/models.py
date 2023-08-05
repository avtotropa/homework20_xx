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


class Version(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    number_version = models.CharField(max_length=150, verbose_name='Номер версии')
    name = models.CharField(max_length=150, verbose_name='Версия')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return f'Курс: {self.course}' \
               f'Версия: {self.number_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
