# Generated by Django 4.2.3 on 2023-07-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Фотография'),
        ),
    ]
